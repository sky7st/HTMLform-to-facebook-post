from __future__ import print_function
import gspread
import json
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials


SHEETID = "1aaB_eVhQ_ql2BJeDstTrsdYfY8CpSwR3xSc-IVr_-No"

def auth_gss_client(path, scopes):
    credentials = ServiceAccountCredentials.from_json_keyfile_name(path,
                                                                   scopes)
    return gspread.authorize(credentials)

def read_sheet(gss_client, key):
    wks = gss_client.open_by_key(key)
    sheet = wks.sheet1
    data = sheet.get_all_records()
    return data

auth_json_path = 'service_ac.json'
gss_scopes = ['https://spreadsheets.google.com/feeds']

gss_client = auth_gss_client(auth_json_path, gss_scopes)

data = read_sheet(gss_client, SHEETID)

for items in data:
    print(items.encode)
