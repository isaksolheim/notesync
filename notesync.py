from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file as oauth_file, client, tools
from apiclient.http import MediaFileUpload
from apiclient import discovery

import sys
from identify import classify

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/drive'

def main(image):
    """Shows basic usage of the Drive v3 API.

    Prints the names and ids of the first 10 files the user has access to.
    """
    store = oauth_file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('drive', 'v3', http=creds.authorize(Http()))

    
    fag = classify(image)

    def uploadFile(filename,filepath,mimetype):
        folder_id = fag
        file_metadata = {
            'name': filename,
            'parents': [folder_id]
        }
        media = MediaFileUpload(filepath,
                            mimetype=mimetype,
                            resumable=True)
        file = service.files().create(body=file_metadata,
                                        media_body=media,
                                        fields='id').execute()
        print('File ID: %s' % file.get('id'))

    uploadFile(image,image,"image/jpeg")

if __name__ == '__main__':
    arguments = sys.argv
    for argument in arguments:
        if argument == sys.argv[0]:
            pass
        else:
            main(argument)

