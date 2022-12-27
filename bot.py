import os
import smtplib
from email.message import EmailMessage
from oculto import senha

#DADOS DO EMAIL DE SEU BOT:
EMAIL_ADDRESS = 'ENDEREÇO DO EMAIL DO BOT'
EMAIL_PASSWORD = senha  #A SENHA É ARMAZENADA EM 'oculto'

#O CORPO DO EMAIL REMETE A MENSAGEM QUE SERÁ ENVIADA E A FORMATAÇÃO DO TEXTO (BASTA UTILIZAR AS TAGS HTML):
corpo_email = """
    <h1>Título</h1>
    <p><b>Parágrafo em negrito</b></p>
    <p>Parágrafo padrão</p>
"""

#CRIAR O EMAIL QUE SERÁ ENVIADO:
msg = EmailMessage()
msg.add_header('Content-Type', 'text/html')
msg.set_payload(corpo_email )
msg['Subject'] = 'ASSUNTO DO EMAIL'
msg['From'] = 'SEU EMAIL DE REMETENTE'
msg['To'] = 'EMAIL DE DESTINATÁRIO'

#CONFIGURAÇÕES E ENVIO DO EMAIL:
with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    smtp.send_message(msg)
