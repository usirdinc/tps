import os
import pickle
import base64
import re
import pyperclip
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.errors import HttpError

# Define the scope and credentials path
creds_path = './credentials.json'
token_path = './fetchtoken.pickle'
scopes = ['https://www.googleapis.com/auth/gmail.readonly']

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

def fetch_verification_code(service):
    try:
        # Search for emails with the specified subject
        results = service.users().messages().list(userId='me', q="subject:Secure two-step verification notification").execute()
        messages = results.get('messages', [])
        
        if not messages:
            print("No verification code emails found.")
            return None, None

        for msg in messages:
            msg_id = msg['id']
            message = service.users().messages().get(userId='me', id=msg_id).execute()
            payload = message['payload']
            headers = payload.get('headers', [])
            email_to = next(header['value'] for header in headers if header['name'] == 'To')

            # Handle both multipart and non-multipart messages
            if 'parts' in payload:
                parts = payload['parts']
                for part in parts:
                    if part['mimeType'] == 'text/plain':
                        msg_str = base64.urlsafe_b64decode(part['body']['data']).decode('utf-8')
                        break
            else:
                msg_str = base64.urlsafe_b64decode(payload['body']['data']).decode('utf-8')

            # Extract verification code from the email body
            match = re.search(r"Please enter this secure verification code: (\d+)", msg_str)
            if match:
                verification_code = match.group(1)
                return verification_code, email_to

        return None, None

    except HttpError as error:
        print(f'An error occurred: {error}')
        return None, None

def main():
    service = get_gmail_service()
    verification_code, email_to = fetch_verification_code(service)
    if verification_code and email_to:
        print(f"Verification code: {verification_code}")
        print(f"Sent to: {email_to}")
        pyperclip.copy(verification_code)
        print("Verification code copied to clipboard.")

if __name__ == '__main__':
    main()
