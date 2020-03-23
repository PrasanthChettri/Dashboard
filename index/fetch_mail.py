#clien ID  =  1086022487863-1cji4srvjudq6854vg12nkbtqmrd6vnr.apps.googleussercontent.com
#Client Secret = BP_CmkhouJrAYkpboe0IryvR 
from __future__ import print_function
import pickle
from os import sys
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
class Gmail:
    def __init__(self):
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

        self.service = build('gmail', 'v1', credentials=creds)
        results = self.service.users().messages().list(userId='me', labelIds = ['INBOX'] ).execute()
        self.messages = results.get('messages', [])

    def sfile(self , num):
        with open('iD' , 'wb') as fh : 
            pickle.dump(num , fh)
        
    def snip(self) : 
        with open('iD' , 'rb') as fh :
            try : 
                a = pickle.load(fh)
            except Exception as e  : 
                self.sfile(0)
                exit()
                a = 0 
        msg_snippets = []
        print("FETCHING MAIL")
        if not self.messages:
            return None
        else:
            first = True
            for message in self.messages:
                msg = self.service.users().messages().get(userId='me', id=message['id']).execute()
                if first : 
                    first = False
                    num = int(msg['internalDate'])
                
                if int(msg['internalDate']) <= a  -1  : 
                    self.sfile(num)
                    break 
                msg_snippets.append(msg['snippet'][:100] + "....")

        return msg_snippets

if __name__ == '__main__':
    a = Gmail()
    print(a.snip())

