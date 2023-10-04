import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SPREADSHEET_ID = "1YKuxPvffbFM6WwXW8fy3Qjk8HE0ZsrHeBKkpuBmirhw"

def refresh_credentials(credentials):
    try:
        credentials.refresh(Request())
    except Exception as e:
        print(f"Error refreshing credentials: {e}")

def get_credentials():
    credentials = None
    if os.path.exists('token.json'):
        credentials = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('secret.json', SCOPES)
            credentials = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(credentials.to_json())
    return credentials

def build_sheets_service():
    credentials = get_credentials()
    if credentials:
        refresh_credentials(credentials)
        service = build('sheets', 'v4', credentials=credentials)
        return service.spreadsheets()
    else:
        print("Failed to obtain valid credentials.")
        return None

def find_empty_row(sheets, column):
    try:
        result = sheets.values().get(spreadsheetId=SPREADSHEET_ID, range=f"🧮 Kalkulyator!A:A").execute()
        values = result.get('values', [])

        # Find the first empty cell in column B
        next_empty_row = 1
        for row in values:
            if row is None:
                break
            next_empty_row += 1

        return next_empty_row
    except HttpError as error:
        print(f"Error finding empty row: {error}")
        return None

def add_row(sheets, new_data, column):
    try:
        next_empty_row = find_empty_row(sheets, column)
        if next_empty_row:
            sheets.values().update(
                spreadsheetId=SPREADSHEET_ID,
                range=f"🧮 Kalkulyator!{column}{next_empty_row}",
                valueInputOption="RAW",
                body={"values": [new_data]}
            ).execute()
            return new_data
        else:
            print('error')
    except HttpError as error:
        print(f"Error adding row: {error}")

def find_row_with_value(sheets, value_to_find, cur):
    try:
        result = sheets.values().get(spreadsheetId=SPREADSHEET_ID, range='🧮 Kalkulyator!A:U').execute()
        values = result.get('values', [])
        for index, row in enumerate(values):
            if row and row[cur] == value_to_find:
                return index + 1, row  # Row numbers start at 1, return the row data as well
        return None, None
    except HttpError as error:
        print(f"Error finding row: {error}")
        return None, None

async def main(search, column, cur):
    try:
        sheets = build_sheets_service()
        if sheets:
            value_to_find = search
            row_number, row_data = find_row_with_value(sheets, value_to_find, cur)
            if row_number:
                if row_data:
                    return row_data
            else:
                new_data = [search]
                data = add_row(sheets, new_data, column)
                row_number, row_data = find_row_with_value(sheets, data[0], cur)
                if row_number:
                    if row_data:
                        return row_data
    except HttpError as error:
        print(error)

async def find_user(value_to_find):
    try:
        sheets = build_sheets_service()
        if sheets:
            result = sheets.values().get(spreadsheetId=SPREADSHEET_ID, range="🏢 Hamkor-do'konlar!A:Z").execute()
            values = result.get('values', [])
            for row in values:
                print(len(row))
                try:
                    if row and str(row[5]) == str(value_to_find):
                        return row  # Row numbers start at 1, return the row data as well
                except (ValueError, IndexError):
                    print(ValueError)  # Row numbers start at 1, return the row data as well
        return None
    except HttpError as error:
        print(f"Error finding row: {error}")
        return None

# if __name__ == "__main__":
#     # Example usage
#     search_value = "YourSearchValue"
#     column_value = "YourColumnValue"
#     cur_value = 5  # Update with the appropriate value
#     result = main(search_value, column_value, cur_value)
#     if result:
#         print(result)
