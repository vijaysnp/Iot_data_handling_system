from pymongo import MongoClient
from pymongo.database import Database
from fastapi import Response
from fastapi import status as st
from apps.utils.standard_response import StandardResponse
from apps.core.mail_service import Maildataservice
from apps.core.send import RabbitmqConfigure, RabbitMq
import logging
import json


class MqttdataService():
    """
    This class is responsible for storing the data in the database
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
                               exchange='')

            rabbitmq = RabbitMq(server)

            rabbitmq.publish(body)
           
            collection = db["tempreature_data_collection"]
            collection.insert_one(body)
           
            # subject = "iot_tempreature_data"
            # html_file = 'confirmation_mail.html'
            # # To render user name & invite link
            # render_args = body
            # reciver_mail_id = body["email"]
            # Maildataservice().send_mail(subject, render_args, html_file, reciver_mail_id)
            
            return StandardResponse(status=st.HTTP_201_CREATED, data=None, message= "data stored in database").make

        except (json.JSONDecodeError, ValueError) as e:
            logging.error(f"Error processing message: {e}")
            return None