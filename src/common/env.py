import os

# Maybe convert this to an enum??
TAB_EVENTS = [
    {"action": "CREATE", "description":"Create a new tab"},
    {"action":"ADD_USER_TO_TAB", "description":"Add a user to an existing tab (by tab id)"},
    {"action":"MAKE_PAYMENT", "description":"Make a payment on an existing tab"},
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