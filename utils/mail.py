from email.mime.text import MIMEText
from smtplib import SMTP

class Mail(object):
    @staticmethod
    def send(sender, recipient, subject, body):
        message = MIMEText(body)
        message['From'] = sender
        message['To'] = recipient
        message['Subject'] = subject
        
        smtp = SMTP('localhost')
        smtp.sendmail(sender, [recipient], message.as_string())
        smtp.quit()
