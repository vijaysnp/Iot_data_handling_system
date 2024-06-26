from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from config import database_config
from fastapi import Depends
from apps.api.schema import Mqttdataschema
from apps.api.services.mqtt_data_handling_service import MqttdataService
from pymongo.mongo_client import MongoClient
from pymongo.database import Database



mqttrouter = InferringRouter()
getdb = database_config.get_db

@cbv(mqttrouter)
class MqttdatahandlingService():


    @mqttrouter.post("/store/tempreture/data")
    async def store_temprature_data(self, body: Mqttdataschema,  db: Database = Depends(getdb)):
        response = MqttdataService().store_temprature_data_service(db, body)
        return response

    @mqttrouter.get("/fetch/current/tempreture")
    async def fetch_current_tempreture(self, db: Database = Depends(getdb)):
        response = MqttdataService().fetch_current_tempreture_service(db)
        return response
       