from fastapi import FastAPI
from config import middleware
from apps.api.view import mqttrouter
# from config import database




# Create the project app
app = FastAPI(title="IOT Data Handling System ", middleware=middleware.middleware_list)


# Load API's
app.include_router(mqttrouter,
                   prefix=f'/v1',
                   tags=['IOT'])

