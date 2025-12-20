# src/utils.py

import os
import gspread
from google.oauth2.service_account import Credentials


def get_sheet(spreadsheet_name: str, worksheet_name: str):
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

    # путь к корню проекта
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    CREDENTIALS_PATH = os.path.join(
        BASE_DIR, "config", "google_credentials.json"
    )

    creds = Credentials.from_service_account_file(
        CREDENTIALS_PATH,
        scopes=scopes
    )

    client = gspread.authorize(creds)
    spreadsheet = client.open(spreadsheet_name)
    return spreadsheet.worksheet(worksheet_name)
