import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Maildataservice():

    def send_email(sender_email, sender_password, recipient_email, subject, message):
        # SMTP server configuration (Gmail SMTP server)
        smtp_server = "smtp.gmail.com"
        smtp_port = 587  # TLS port

        # Create a multipart message
        email_message = MIMEMultipart()
        email_message['From'] = sender_email
        email_message['To'] = recipient_email
        email_message['Subject'] = subject

        # Attach the message to the email
        email_message.attach(MIMEText(message, 'plain'))

        try:
            # Connect to the SMTP server
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()  # Start TLS encryption
            # Login to the SMTP server
            server.login(sender_email, sender_password)
            # Send email
            server.sendmail(sender_email, recipient_email, email_message.as_string())
            print("Email sent successfully!")
        except Exception as e:
            print("Failed to send email:", e)
        finally:
            # Quit SMTP session
            server.quit()
