import json
import requests
from fastapi.encoders import jsonable_encoder
from pymongo import MongoClient
from pymongo.database import Database
from fastapi import Response
from fastapi import status as st
from apps.utils.standard_response import StandardResponse
from apps.core.mail_service import Maildataservice
from apps.core.publish_message import RabbitmqConfigure, RabbitMq
from apps.core.subscribe_message import RabbitMqServerConfigure, rabbitmqServer

# Weather API configuration (replace with your API key)
WEATHER_API_URL = 'https://api.openweathermap.org/data/2.5/weather'
WEATHER_API_KEY = 'WEATHER_API_KEY'


class MqttdataService():
    """
    This class is responsible for handling Rabbit mqtt messages
    """
    def __init__(self):
        pass

    def store_temprature_data_service(self, db: Database, body: dict):
        """
        This method is responsible for sProcesses an incoming MQTT message.
        :param db: Database object
        :param body: Body of the request
        :return: 
            dict: The processed message data or None if processing fails.
        """
        try:
            body = body.dict()

            server = RabbitmqConfigure(queue='hello',
                               host='localhost',
                               routingKey='hello',
                               exchange='amq.topic',
                               exchange_type='topic')

            rabbitmq = RabbitMq(server)
            rabbitmq.publish(body) 
            collection = db["tempreature_data_collection"]
            collection.insert_one(body)   
            return StandardResponse(status=st.HTTP_201_CREATED, data=None, message= "data stored in database").make

        except Exception as e:
            return StandardResponse(status.HTTP_400_BAD_REQUEST, 
                                    constant.STATUS_NULL, ErrorMessage.somethingWentWrong).make


    def fetch_current_tempreture_service(self, db: Database):
        """
        This method is responsible for sProcesses an incoming MQTT message.
        :param db: Database object
        :return: 
            dict: The processed message data or None if processing fails.
        """
        try:
            serverconfigure = RabbitMqServerConfigure(host='localhost',
                                              queue='hello')

            server = rabbitmqServer(server=serverconfigure)
            server.startserver()
            
            if server.payload:
                processed_data = ast.literal_eval(server.payload)

                city_name = processed_data["city"]

                temperature = self.fetch_temperature(city_name)
                if isinstance(temperature, str):
                    return StandardResponse(status=st.HTTP_404_NOT_FOUND, data=None, message= "Error fetching temperature").make
    
                else:
                    subject = "Current Temperature"
                    message = f"Subject: Current Temperature in {city_name}\n\nThe current temperature in {city_name} is \
                    {temperature:.2f} degrees Celsius."
                    sender_email = "noreply@example.com"
                    recipient_email = processed_data["recipient_email"]

                    Maildataservice().send_email(sender_email, sender_password, recipient_email, subject, message)  
                    return StandardResponse(status=st.HTTP_200_OK, data=None, message= "mail sent Successfully").make
            else:
                return StandardResponse(status=st.HTTP_404_NOT_FOUND, data=None, message= "payload not fount").make
    
        except Exception as e:
            return StandardResponse(status.HTTP_400_BAD_REQUEST, 
                                    constant.STATUS_NULL, ErrorMessage.somethingWentWrong).make


    def fetch_temperature(city_name):
        """Fetches the current temperature for a given city using the weather API."""
        url = f"{WEATHER_API_URL}?q={city_name}&appid={WEATHER_API_KEY}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            return data["main"]["temp"] - 273.15  # Convert Kelvin to Celsius
        else:
            return f"Error: Could not fetch temperature for {city_name} (status code: {response.status_code})"
