import json
from time import sleep

import httplib2, os
from google.auth.exceptions import RefreshError

from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import run_flow
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

import files

CLIENT_SECRET = files.get_credentials('client_secret_desktop.json')
RW_SCOPE = 'https://www.googleapis.com/auth/drive'
STORAGE = Storage(files.get_credentials('communication_drive_credentials.storage'))

__default_drive = None

__list_of_folder = ['post']

# Start the OAuth flow to retrieve credentials
def authorize_credentials():
  # Fetch credentials from storage
  credentials = STORAGE.get()
  # If the credentials doesn't exist in the storage location then run the flow
  if credentials is None or credentials.invalid:
    flow = flow_from_clientsecrets(CLIENT_SECRET, scope=RW_SCOPE)
    http = httplib2.Http()
    credentials = run_flow(flow, STORAGE, http=http)
  return credentials

def main():
  # credentials = authorize_credentials()
  get_drive()
  # print(credentials)

def get_drive(drive=None):
  if not drive:
    auth = GoogleAuth()
    auth.LoadCredentialsFile(files.get_credentials('communication_drive_credentials.storage'))
    if auth.access_token_expired:
      # Refresh them if expired
      try:
        auth.Refresh()
      except RefreshError as e:
        print("Google Drive error: %s", e)
      except Exception as e:
        print(e)
    else:
      # Initialize the saved creds
      auth.Authorize()
    _drive = GoogleDrive(auth)
    return _drive

  if drive.auth.access_token_expired:
    try:
      drive.auth.Refresh()
    except RefreshError as e:
      print("Google Drive error: %s", e)
  return drive

def create_drive_folder(to_created=False):
  if to_created:
    for file_name in __list_of_folder:
      path = files.get_drive(file_name)
      if not os.path.exists(path):
        drive = get_drive()
        exist = drive.ListFile({'q': f"title='{file_name}' and mimeType='application/vnd.google-apps.folder' and trashed=false"})
        if not exist.items():
          file_drive = get_drive().CreateFile({'title': file_name, 'mimeType': 'application/vnd.google-apps.folder'})
          file_drive.InsertPermission({
            'type': 'user',
            'value': 'user',
            'role': 'owner'})
          file_drive.Upload()
          sleep(2)
          f = open(path, "w+")
          file_drive.FetchMetadata(fetch_all=True)
          f.write(json.dumps(file_drive.metadata, indent=2))
          f.close()
