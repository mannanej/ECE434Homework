#!/usr/bin/env python3
from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import time, sys
from subprocess import call
import Adafruit_BBIO.GPIO as GPIO

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1pMI8vsJR60noMGI1sj3RFM72_DkGCPsmEoVyC0m0S8s'
SAMPLE_RANGE_NAME = 'A2'

def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            # creds = flow.run_local_server(port=0)
            creds = flow.run_console()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    while (True):
        values = [ [time.time()/60/60/24+ 25569 - 5/24, getLeft(), getMiddle(), getRight()]]
        body = {'values': values}
        result = sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME,
                                valueInputOption='USER_ENTERED', 
                                body=body
                                ).execute()
        print(result)

def getLeft():
    with open("/sys/class/hwmon/hwmon2/temp1_input", 'r') as f:
        # this chunk converts it from the base value to F
            milliC = f.readline(-1)
            milliC = int(milliC)
            # print(milliC)
            normalC = milliC / 1000
            # print(normalC)
            normalFLeft = (normalC * (9 / 5) + 32)
            # print("Left Sensor: ", normalF)
            f.close()
    return round(normalFLeft, 2)

def getMiddle():
    with open("/sys/class/hwmon/hwmon0/temp1_input", 'r') as f:
        # this chunk converts it from the base value to F
            milliC = f.readline(-1)
            milliC = int(milliC)
            # print(milliC)
            normalC = milliC / 1000
            # print(normalC)
            normalFMiddle = (normalC * (9 / 5) + 32)
            # print("Right Sensor: ", normalF)
            f.close()
    return round(normalFMiddle, 2)

def getRight():
    with open("/sys/class/hwmon/hwmon1/temp1_input", 'r') as f:
        # this chunk converts it from the base value to F
            milliC = f.readline(-1)
            milliC = int(milliC)
            # print(milliC)
            normalC = milliC / 1000
            # print(normalC)
            normalFRight = (normalC * (9 / 5) + 32)
            # print("Middle Sensor: ", normalF)
            f.close()
    return round(normalFRight, 2)

if __name__ == '__main__':
    main()
