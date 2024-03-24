from pymongo import MongoClient
from pymongo.database import Database
from fastapi import Response
import logging





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
            body_test = body.get('city', None)
            collection = db["vijay_collection"]
            collection.insert_one(body)
            message = "data stored in database"
            
            return Response(status_code=200, content=message)
        except (json.JSONDecodeError, ValueError) as e:
            logging.error(f"Error processing message: {e}")
            return None