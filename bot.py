import os
import smtplib
from email.message import EmailMessage
from oculto import senha

EMAIL_ADDRESS = 'bote54893@gmail.com'
EMAIL_PASSWORD = senha

corpo_email = """
    <h1>AAAAAAAA</h1>
    <p><b>UUUUUUUUU</b></p>
    <p>aaaaaaaaaa</p>
    """

msg = EmailMessage()
msg.add_header('Content-Type', 'text/html')
msg.set_payload(corpo_email )
msg['Subject'] = 'Teste Message Automatic'
msg['From'] = 'bote54893@gmail.com'
msg['To'] = 'murilo.zague@etec.sp.gov.br'

with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    smtp.send_message(msg)