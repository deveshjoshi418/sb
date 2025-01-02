import gspread
from oauth2client.service_account import ServiceAccountCredentials
import streamlit as st

# Define the scope and authenticate with the credentials
scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# Open the Google Sheet by name
sheet = client.open("Your Sheet Name").sheet1

# Fetch all records from the sheet
data = sheet.get_all_records()

# Streamlit interface
st.title('Google Sheets with gspread')

# Display the data in a table format
st.write(data)
