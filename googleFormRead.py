#coding=utf-8
from __future__ import print_function
import gspread
import json
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials


SHEETID = "1FVSpACCghxbrOe0vFxWjy0tLFL8kWWytznuj56BW0TQ"
auth_json_path = 'service_ac.json'
gss_scopes = ['https://spreadsheets.google.com/feeds']


def auth_gss_client(path, scopes):
    credentials = ServiceAccountCredentials.from_json_keyfile_name(path,
                                                                   scopes)
    return gspread.authorize(credentials)

def read_sheet(gss_client, key):
    wks = gss_client.open_by_key(key)
    sheet = wks.sheet1
    
    return sheet



gss_client = auth_gss_client(auth_json_path, gss_scopes)

sheet = read_sheet(gss_client, SHEETID)
data = sheet.get_all_records()

table = pd.DataFrame(sheet.get_all_records())

# for items in data:
#     print(items)

# sheet.clear()
print(sheet.title)