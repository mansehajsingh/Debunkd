from flask_mail import Mail, Message
import os

class MailHandler:

    mail = None

    def __init__(self, app) -> None:
        #configuring email settings
        app.config['MAIL_SERVER'] = "smtp.gmail.com"
        app.config['MAIL_PORT'] = 465
        app.config['MAIL_USE_TLS'] = False
        app.config['MAIL_USE_SSL'] = True
        app.config['MAIL_USERNAME'] = os.environ.get('DebunkdEmailUser') # OS ENVIRONMENT VARIABLES USED TO NOT HARDCODE
        app.config['MAIL_PASSWORD'] = os.environ.get('DebunkdEmailPass') # DETAILS. WILL NOT WORK ON DEPLOYMENT.

        self.mail = Mail(app)

    def send_message(self, app, name, email, subject, body):
        message = Message( # constructing the message
            subject = subject, 
            sender = app.config.get("MAIL_USERNAME"),
            recipients = [app.config.get("MAIL_USERNAME")],
            body = f"User Email: {email}\n User Name: {name}\n Body:\n\n{body}"
        )

        self.mail.send(message)
