import hou
import os
import sys

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import httplib2
from google_auth_httplib2 import AuthorizedHttp

creds = service_account.Credentials.from_service_account_file('/usr/people/yasunaga/houdini20.0/python3.9libs/up_gb/keyfile.json', scopes = ['https://www.googleapis.com/auth/drive'])
drive_service  = build('drive', 'v3', credentials=creds)

load_path = hou.pwd().parm("Loaded_File").evalAsString()

file_name = load_path.split("/")[-1]
file_metadata = {
    'name': file_name,
    'parents': ['14h_NJPUMsbSj7ryjfxiATDr8Tl_Xt9cw'],
}

media = MediaFileUpload(load_path, mimetype='application/py')
file = drive_service.files().create(body = file_metadata, media_body = media, fields = 'id', supportsAllDrives = True).execute()

print(f'File ID: {file.get("id")}') 

#googlde drive share link = https://drive.google.com/drive/folders/14h_NJPUMsbSj7ryjfxiATDr8Tl_Xt9cw?usp=drive_link
#github link = https://github.com/allfreeman/HoudiniUtils
