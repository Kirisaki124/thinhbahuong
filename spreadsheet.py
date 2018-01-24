from __future__ import print_function
import argparse
import time

from apiclient import discovery
from httplib2 import Http
from oauth2client import file, tools, client

SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
store = file.Storage('storage.json')
creds = store.get()

flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
flow = client.flow_from_clientsecrets('client_secret.json',SCOPES)
creds = tools.run_flow(flow,store,flags)

service = discovery.build('sheets', 'v4', http=creds.authorize(Http()))
# spreadsheet_body = {'properties': {'title': 'Thính bà Hương [%s]' % time.ctime}}
#
# request = service.spreadsheets().create(body=spreadsheet_body).execute()
# SHEET_ID = request['spreadsheetId']
# print('Created "%s"' % request['properties']['title'])
