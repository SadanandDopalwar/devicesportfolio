import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
# Email credentials
sender_email = ""
sender_password = ""   # Use the App Password, not the regular password
receiver_email = ""
cc_emails = ""

# Email content
subject = "Test Email from Python"
body = "This is a test email sent using Python."
isattachments = True  # Set to True if you want to include attachments
# Construct the email
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Cc"] = cc_emails
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))


if isattachments:
    for filename in os.listdir('.'):
            if filename.endswith('.png'):
                with open(filename, 'rb') as attachment:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header(
                    'Content-Disposition',
                    f'attachment; filename="{filename}"',
                )
                message.attach(part)
# Send the email
try:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(message)
        print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
