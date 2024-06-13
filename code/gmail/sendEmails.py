import os
import pickle
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from google.auth.transport.requests import Request
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
# Define the scope and credentials path
creds_path = './credentials.json'
token_path = './sendtoken.pickle'
scopes = ['https://www.googleapis.com/auth/gmail.send']

def get_gmail_service():
    creds = None
    # Load the token from the file if it exists
    if os.path.exists(token_path):
        with open(token_path, 'rb') as token:
            creds = pickle.load(token)
    # If there are no valid credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(creds_path, scopes)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(token_path, 'wb') as token:
            pickle.dump(creds, token)
    service = build('gmail', 'v1', credentials=creds)
    return service

def create_message(sender, to, subject, message_text):
    # Create message
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = to
    message['Subject'] = subject
    message.attach(MIMEText(message_text, 'html'))
    raw = base64.urlsafe_b64encode(message.as_bytes())
    raw = raw.decode()
    return {'raw': raw}

def send_message(service, user_id, message):
    try:
        message = (service.users().messages().send(userId=user_id, body=message).execute())
        return message
    except HttpError as error:
        print(f'An error occurred: {error}')

def main():
    email = input("Enter your gmail address: ")
    name = input("Enter your name: ")
    service = get_gmail_service()
    
    # Read the HTML template from the file
    with open('./templates/biometric_notice_email.html', 'r') as file:
        email_template = file.read()
    
    # Define the dynamic content
    dynamic_content = {
        "email" : email,
        "recipient_name": name,
        "date": "06/05/2024",
        "time": "10:00 AM",
        "location": "USCIS Long Island City",
        "link": "www.google.com",
    }
    
    # Replace placeholders with dynamic content
    email_body = email_template.format(**dynamic_content)
    
    message = create_message(
        "immigration@usird.org", 
        dynamic_content['email'], 
        f"Biometric Appointment Notification - {dynamic_content['recipient_name']}", 
        email_body
    )
    send_message(service, "me", message)

main()