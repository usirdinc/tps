import os
import pickle
import io
from datetime import datetime
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/drive']

def get_drive_service():
    """Authenticate and return a Google Drive service object."""
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return build('drive', 'v3', credentials=creds)

def fetch_files(service, local_folder, folder_id='root'):
    query = f"'{folder_id}' in parents and trashed=false"
    results = service.files().list(q=query, pageSize=100, fields="nextPageToken, files(id, name, mimeType, modifiedTime)").execute()
    items = results.get('files', [])

    if not items:
        print('No files found in folder:', local_folder)
    else:
        for item in items:
            file_id = item['id']
            file_name = item['name']
            mime_type = item['mimeType']
            file_path = os.path.join(local_folder, file_name)

            if mime_type == "application/vnd.google-apps.folder":
                new_folder = os.path.join(local_folder, file_name)
                if not os.path.exists(new_folder):
                    os.makedirs(new_folder)
                fetch_files(service, new_folder, file_id)  # Recursively fetch contents
            elif "google-apps" in mime_type:
                print(f"Skipping Google Doc format file: {file_name}")
            else:
                if os.path.exists(file_path):
                    local_mod_time = os.path.getmtime(file_path)
                    drive_mod_time = datetime.fromisoformat(item['modifiedTime'].replace('Z', '+00:00')).timestamp()
                    if local_mod_time >= drive_mod_time:
                        print(f"Skipping download, local file is up to date: {file_name}")
                        continue
                download_file(service, file_id, file_path, item['modifiedTime'])
                print(f"Downloaded {file_name} from Google Drive.")

def download_file(service, file_id, file_path, modified_time_str):
    request = service.files().get_media(fileId=file_id)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while not done:
        status, done = downloader.next_chunk()
    with io.open(file_path, 'wb') as f:
        fh.seek(0)
        f.write(fh.read())
    modified_time = datetime.fromisoformat(modified_time_str.replace('Z', '+00:00'))
    os.utime(file_path, (modified_time.timestamp(), modified_time.timestamp()))


def push_files_recursive(service, local_folder, parent_id='root'):
    """Recursively upload files and folders to Google Drive, maintaining the folder structure."""
    for entry in os.listdir(local_folder):
        full_path = os.path.join(local_folder, entry)
        if os.path.isfile(full_path):
            if not check_file_exists(service, entry, parent_id):
                file_metadata = {'name': entry, 'parents': [parent_id]}
                media = MediaFileUpload(full_path, mimetype='application/octet-stream')
                file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
                print(f"Uploaded {entry} to Google Drive with ID {file['id']}")
            else:
                print(f"Skipping upload, file already exists on Drive: {entry}")
        elif os.path.isdir(full_path):
            print(f"Entering directory: {entry}")
            new_parent_id = find_or_create_folder(service, entry, parent_id)
            push_files_recursive(service, full_path, new_parent_id)  # Recursive call with new parent ID

def check_file_exists(service, file_name, parent_id):
    """Check if file exists on Google Drive."""
    query = f"name='{file_name}' and '{parent_id}' in parents and trashed=false"
    response = service.files().list(q=query, fields='files(id, name)').execute()
    files = response.get('files', [])
    return files[0]['id'] if files else None

def find_or_create_folder(service, folder_name, parent_id='root'):
    """Find or create a folder on Google Drive."""
    query = f"mimeType='application/vnd.google-apps.folder' and name='{folder_name}' and '{parent_id}' in parents and trashed=false"
    response = service.files().list(q=query, fields='files(id, name)').execute()
    files = response.get('files', [])
    if not files:
        folder_metadata = {'name': folder_name, 'mimeType': 'application/vnd.google-apps.folder', 'parents': [parent_id]}
        folder = service.files().create(body=folder_metadata, fields='id').execute()
        return folder.get('id')
    else:
        return files[0]['id']

google_drive_folder_id = '15PnrY_VxCulWn2awuTibOR-YGILTwQKu'
local_sync_folder = '../Notice'

if __name__ == '__main__':
    service = get_drive_service()
    if not os.path.exists(local_sync_folder):
        os.makedirs(local_sync_folder)
    fetch_files(service, local_sync_folder, google_drive_folder_id)
    push_files_recursive(service, local_sync_folder, google_drive_folder_id)

