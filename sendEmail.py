import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())  # reads the text in html and makes it a template

email = EmailMessage()
email['from'] = 'Abc abc'
email['to'] = 'abc@gmail.com'
email['subject'] = 'Hey it\'s me'

email.set_content(html.substitute({'name' : 'ABC'}), 'html')

with smtplib.SMTP(host = 'smtp.gmail.com', port = 587) as smtp:  # host is custom for each platform
    smtp.ehlo()  # starts smtp
    smtp.starttls()  # starts security encryption
    smtp.login('youremail@gmail.com', 'Yourpasswordhere')
    smtp.send_message(email)
    print('Email sent succesfully !!')