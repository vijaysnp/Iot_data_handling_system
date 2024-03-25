import os
import smtplib
from jinja2 import Environment       
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Maildataservice():

    def __init__(self):
        self.server = ""
        self.port = ""
        self.user = ""
        self.password = ""
        self.sender = ""
        
    def send_mail(self,
        subject: str,
        render_args: dict,
        html_file: str,
        receiver_email: str):
        """
        This function is used to send email with respect
        to render information & html file.

        Args:
            render_args(dict): render arguments
            subject(str): The email subject
            html_file(str): Html file name
            receiver_email(str): The email address of recipient

        Returns:
            send a reset password email to user
        """
        message = MIMEMultipart("alternative")
        message["Subject"] = subject
        message["From"] = self.sender
        message["To"] = receiver_email

        current_directory = os.getcwd()
        html = open(f'{os.getcwd()}/assets/templates/{html_file}').read()
        
        # Create a text/html message from a rendered subject
        message.attach(MIMEText(Environment().from_string(html).render(**render_args),"html"))

        # Send email
        with smtplib.SMTP_SSL(self.server, self.port) as server:
            server.login(self.user, self.passwordss)
            server.sendmail(
                mail_config.SENDER_EMAIL,
                receiver_email,
                message.as_string().encode("utf-8"))
