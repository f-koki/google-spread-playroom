import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'upheld-altar-263406-906f403b7fff.json', scope)
gc = gspread.authorize(credentials)
wks = gc.open('spread-sample').sheet1

wks.update_acell('A1', 'Hello World')
print(wks.acell('A1'))
