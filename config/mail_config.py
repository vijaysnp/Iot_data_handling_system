
import os

# Smtp email sending credentials
SMTP_SERVER = os.environ.get('SMTP_SERVER')
SMTP_PORT = (os.environ.get('SMTP_PORT'))
SMTP_USERNAME = os.environ.get('SMTP_USERNAME')
SMTP_PASSWORD = os.environ.get('SMTP_PASSWORD')
SENDER_EMAIL = os.environ.get('SENDER_EMAIL')

# Route for sending mail
FORGET_ROUTE = os.environ.get('FORGET_ROUTE')