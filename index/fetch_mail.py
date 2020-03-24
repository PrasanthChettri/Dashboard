#clien ID  =  1086022487863-1cji4srvjudq6854vg12nkbtqmrd6vnr.apps.googleussercontent.com
#Client Secret = BP_CmkhouJrAYkpboe0IryvR 
import pickle
import re
from os import sys
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
from .models import models

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
        self.thrd_dict = results.get('messages', [])
        self.pre_stuff()

    def sfile(self , num):
        with open('iD' , 'wb') as fh : 
            pickle.dump(num , fh)

    def pre_stuff(self) : 
            try : 
                with open('iD' , 'rb') as fh :self.a = pickle.load(fh)
            except Exception as e  : 
                self.a = 0 

    def save_recent(self ):
        print(self.dict_id)
        msg_obj = self.service.users().messages().get(userId='me', id= self.dict_id[0]).execute()
        self.sfile(int(msg_obj['internalDate']))

    def clean(self , string) :
        regex = re.compile('&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
        cleantext = re.sub(regex , '' , string)
        return cleantext

    def get_snipped_messages(self):
        self.dict_id = {}
        msg_snippets = []
        self.messages  = []
        msg_titles = []
        print("FETCHING MAIL")
        if not self.thrd_dict:
            return None
        else :
            for i , message in enumerate(self.thrd_dict):
                msg = self.service.users().messages().get(userId='me', id=message['id']).execute()
                print(msg)
                msg_title = list(filter(lambda x : x['name'] == 'From' , msg['payload']['headers']))[0]['value']
                msg_date =  int(msg['internalDate'])
                self.dict_id[i] = msg['id']
                msg_i = self.clean(msg['snippet'])
                if msg_date <= int(self.a) - 1  : break 
                msg_snippets.append([msg_title , msg_i])

        self.save_recent()
        return msg_snippets

if __name__ == '__main__':
    a = Gmail()
    print(a.snip())
