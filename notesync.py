from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file as oauth_file, client, tools
from apiclient.http import MediaFileUpload
from apiclient import discovery

from PIL import Image

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/drive'

# folder ids
matte = "1TRQLR9GuNpmGa2CaGEJNlNzHkezDFZpg"
fysikk = "19YX0I_o7h5rYkTv_oEWNIepEt7mc7wx7"
    
fag = []
def classifier():
    img = Image.open("blue.jpg")

    #resize to smaller image
    w,h = img.size
    img.resize((w/10,h//10)).save("tmp.jpg")
    img.close()

    #open new image
    img = Image.open("tmp.jpg")
    pix = img.load
    
    w,h = img.size

    blue = [range(60,90), range(110,140), range(110,140)]
    red = [range(180,230), range(70,115), range(30,70)]
    green = [range(130,170),range(140,180), range(60,85)]
    yellow = [range(200,235), range(180,210), range(95,120)]
    pink = [range(210,240), range(150,180), range(110,130)]


    
    #check pixel rgb value, append blues to list
    for y in range(h):
        for x in range(w):
            r,g,b = pix[x,y]
            if r in blue[0] and g in blue[1] and b in blue[2]: 
                print("BLUE",x,y)
                fag.append(matte)
                break
            elif r in red[0] and g in red[1] and b in red[2]:
                print("RED",x,y)
                fag.append(fysikk)
                break
            elif r in green[0] and g in green[1] and b in green[2]:
                print("GREEN", x,y)
                break
            elif r in yellow[0] and g in yellow[1] and b in yellow[2]:
                print("YELLOW",x,y)
                break
            elif r in pink[0] and g in pink[1] and b in pink[2]:
                print("PINK",x,y)
                break
            else:
                pass
        
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

    uploadFile("blue.jpg","blue.jpg","image/jpeg")
if __name__ == '__main__':
    main()
