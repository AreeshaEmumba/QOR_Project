import subprocess
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import logging

logging.basicConfig(filename='send_email.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', filemode='w')

# Email details
sender = 'areesha.mahmood@emumba.com'
receiver = 'areesha.mahmood@emumba.com'
subject = 'HTML API Test Results'
body = 'Attached are the latest API test results in HTML format.'
attachment = '/home/emumba/Desktop/QOR_Project/Postman/newman_results.html'

logging.info(f"sender = {sender}")
logging.info(f"receiver = {receiver}")
logging.info(f"subject = {subject}")
logging.info(f"body = {body}")
logging.info(f"attachment = {attachment}")

# Create the MIME message
msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = receiver
msg['Subject'] = subject

# Attach the body of the email as plain text
msg.attach(MIMEText(body, 'plain'))

# Attach the file
with open(attachment, 'rb') as f:
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(f.read())
    encoders.encode_base64(part)
    part.add_header(
        'Content-Disposition',
        f'attachment; filename={os.path.basename(attachment)}'
    )
    msg.attach(part)

# Convert the message to a string
message = msg.as_string()

# Use subprocess to call msmtp to send the email
try:
    process = subprocess.Popen(
    ['msmtp', '--debug', receiver],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
    )
     
    # Logging the process for debugging
    logging.info(f"process = {process}")
    
    # Communicate with msmtp using echo
    process.communicate(input=message.encode())
    logging.info("Email sent successfully!")
    print("Email sent successfully!")
except Exception as e:
    logging.error(f"An error occurred: {e}")
    print(f"An error occurred: {e}")
