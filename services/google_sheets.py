import logging
from google.oauth2 import service_account
from googleapiclient.discovery import build
import os
import streamlit as st
from typing import List, Any

@st.cache_resource
def get_sheets_service():
    """Cache Google Sheets service configuration"""
    try:
        import json
        if "GOOGLE_SHEETS_CREDENTIALS_JSON" in st.secrets:
            creds_dict = json.loads(st.secrets["GOOGLE_SHEETS_CREDENTIALS_JSON"])
            creds = service_account.Credentials.from_service_account_info(
                creds_dict,
                scopes=['https://www.googleapis.com/auth/spreadsheets']
            )
        else:
            creds = service_account.Credentials.from_service_account_file( # type: ignore
                os.getenv('GOOGLE_SHEETS_CREDENTIALS'), 
                scopes=['https://www.googleapis.com/auth/spreadsheets']
            )
        service: Any = build('sheets', 'v4', credentials=creds)
        return service
    except Exception as e:
        raise e
