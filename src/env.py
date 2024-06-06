import os

TAB_EVENTS = [
    {"action": "CREATE", "description":"Create a new tab"},
    {"action":"UPDATE", "description":"Update an existing tab (make payment, add user)"},
    {"action":"DELETE", "description":"Delete an existing tab"},
    {"action":"GET", "description":"Retrieve an existing tab"}
]

def get_users_table_name():
    return ""

def get_tabs_table_name():
    return ""

def get_payments_table_name():
    return ""

def get_events_table_name():
    return ""

def get_files_dir(file_type):
    return f"{file_type}/"

def get_token():
    return os.getenv('TOKEN')