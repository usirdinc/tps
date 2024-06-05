import os
import pickle
import base64
import email
from bs4 import BeautifulSoup
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

# Define your scope and credentials file
creds_path = './credentials.json'
token_path = './token.pickle'
scopes = ['https://www.googleapis.com/auth/gmail.readonly']

def get_gmail_service():
    creds = None
    if os.path.exists(token_path):
        with open(token_path, 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(creds_path, scopes)
            creds = flow.run_local_server(port=0)
        with open(token_path, 'wb') as token:
            pickle.dump(creds, token)
    return build('gmail', 'v1', credentials=creds)

def get_mime_message(service, user_id, msg_id):
    message = service.users().messages().get(userId=user_id, id=msg_id, format='raw').execute()
    msg_str = base64.urlsafe_b64decode(message['raw'].encode('ASCII'))
    mime_msg = email.message_from_bytes(msg_str)
    return mime_msg

def parse_html_content(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    payment_note = soup.select_one('.tblMobZ3Content9CenterNoPadding')
    if payment_note:
        notes = payment_note.text.strip()
        if "Please allow up to 5 minutes for the money to deposit to your account." in notes:
            return ""  # Leave note blank if it contains the specific sentence
        return notes
    return "No payment note found"

def extract_subject_info(subject):
    parts = subject.split(" sent you $")
    sender = parts[0].strip() if parts else "Unknown sender"
    amount = f"${parts[1].strip()}" if len(parts) > 1 else "Unknown amount"
    return sender, amount

def list_messages(service, user_id):
    query = 'from:customerservice@ealerts.bankofamerica.com'
    results = service.users().messages().list(userId=user_id, q=query, maxResults=1000).execute()
    messages = results.get('messages', [])
    html_output = "<html><body><table><tr><th>Sender</th><th>Notes</th><th>Amount</th><th>Date</th></tr>"

    if not messages:
        print("No messages found from Bank of America.")
        return

    for message in messages:
        mime_msg = get_mime_message(service, user_id, message['id'])
        subject = mime_msg['subject']
        sender, amount = extract_subject_info(subject)
        date = mime_msg['date']  # Extract date from email headers

        if mime_msg.is_multipart():
            for part in mime_msg.walk():
                if 'text/html' in part.get_content_type():
                    html_content = part.get_payload(decode=True).decode()
                    notes = parse_html_content(html_content)
                    row = f"<tr><td>{sender}</td><td>{notes}</td><td>{amount}</td><td>{date}</td></tr>"
                    html_output += row
        else:
            content_type = mime_msg.get_content_type()
            if 'text/html' in content_type:
                html_content = mime_msg.get_payload(decode=True).decode()
                notes = parse_html_content(html_content)
            else:
                notes = "HTML content not found"
            row = f"<tr><td>{sender}</td><td>{notes}</td><td>{amount}</td><td>{date}</td></tr>"
            html_output += row

    html_output += "</table></body></html>"
    save_as_html(html_output)

def save_as_html(content):
    with open("emails.html", "w") as file:
        file.write(content)

def main():
    service = get_gmail_service()
    list_messages(service, 'me')

if __name__ == '__main__':
    main()
