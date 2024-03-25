import os
from dotenv import load_dotenv
from os.path import join
from .project_path import BASE_DIR


# ##### ENV CONFIGURATION ################################

# Take environment variables from .env file
dotenv_path = join(BASE_DIR, '.env')
load_dotenv(dotenv_path)


MONGO_URL = os.environ.get('MONGO_URL')