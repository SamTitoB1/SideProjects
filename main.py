import smtplib
# Importing libraries for including email transmission and atatchements
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart



# Simple Mail Transfer Protocol
# Log into gmail SMTP sever

server = smtplib.SMTP('smtp.gmail.com',465)
# Starting the process
server.ehlo()

# Logging with credentials to Google mailing service
server.login('876ncos@gmail.com','eightsevensix')

# A better practice is to open an encrypted file containing the user and pass
# with open('FILENAMEHERE.txt','r') as f:
#       password = f.read()

msg = MIMEMultipart()
# Defining the header for sending
msg['From'] = 'Future Self'
msg['To'] = 'blackribbonevnts@gmail.com'
msg['Subject'] = 'Important Business'

with open('message.txt', 'r') as f:
    message = f.read()

# Adding our message through with the converter MIMEText, and sub-type of plain
msg.attach(MIMEText(message, 'plain'))

# Attaching a image to the email

filename = 'HelloLight_Mac.png'
# SInce image type we want to read as bytes
attachment = open(filename,'rb')

# Since pulled as bytes, we are now sending insturctions to read as bytes
picture = MIMEBase('application', 'octet-stream')
picture.set_payload(attachment.read())

# Use of encoders to tell the Layer 7 to read
encoders.encode_base64(picture)
picture.add_header('Content-Disposition', f'attachment; filename={filename}')

msg.attach(picture)

text = msg.as_string()

server.sendmail('876ncos@gmail.com', 'blackribbonevnts@gmail.com', text)


# ERROR WITH SMTP FOR


