import os
import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

contacts = ['ccwash03@gmail.com', EMAIL_ADDRESS]

msg = EmailMessage()
msg['Subject'] = 'Do you want to grab dinner this weekend?'
msg['From'] = EMAIL_ADDRESS
msg['To'] = contacts
msg.set_content('Does any of this food sound good to you? I made a list of each of their respective restaurants in the attachment.')

files = ['spaghetti.jpg', 'soup.jpg', 'tea.jpg', 'pancakes.png']
docs = ['test.docx']
for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name
    
    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)
    
for file in docs:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_name = f.name
    
    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
    
    