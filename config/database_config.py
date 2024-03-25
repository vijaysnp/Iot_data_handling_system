import os
from config import env_config
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

# ##### DATABASE CONFIGURATION ############################
# MONGO_URL = os.environ.get('MONGO_URL')

MONGO_URL = "mongodb://127.0.0.1:27017/"


# client = MongoClient(MONGO_URL)
# db = client[os.environ.get('MONGO_INITDB_DATABASE')]

def get_db():
    try:
        client = MongoClient(MONGO_URL)
        db = client["vijay"]
        yield db
    finally:
        client.close()

# if __name__ == "__main__":
#     client = None
#     try:
#         client = MongoClient(MONGO_URL)
#         db = client["vijay"]
#         collection = db["vijay_collection"]
#         collection.insert_one({"name": "vijay", "age":25})
#     finally:
#         if client:
#             client.close()