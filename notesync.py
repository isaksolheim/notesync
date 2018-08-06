from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file as oauth_file, client, tools
from apiclient.http import MediaFileUpload
from apiclient import discovery

import cv2
import numpy as np

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/drive'

# folder ids
matte = "1TRQLR9GuNpmGa2CaGEJNlNzHkezDFZpg"
fysikk = "19YX0I_o7h5rYkTv_oEWNIepEt7mc7wx7"
    
fag = []
def classifier():
    img = cv2.imread("IMG_3682.JPG")
    blue = img[100,0,0]
    
    if blue <= 50:
        fag.append("1TRQLR9GuNpmGa2CaGEJNlNzHkezDFZpg")
    else:
        fag.append( "19YX0I_o7h5rYkTv_oEWNIepEt7mc7wx7")
classifier()
print(fag)

def main():
    """Shows basic usage of the Drive v3 API.

    Prints the names and ids of the first 10 files the user has access to.
    """
    store = oauth_file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('drive', 'v3', http=creds.authorize(Http()))

    def uploadFile(filename,filepath,mimetype):
        folder_id = fag[0]
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

    uploadFile("IMG_3682.JPG","IMG_3682.JPG","image/jpeg")
if __name__ == '__main__':
    main()
