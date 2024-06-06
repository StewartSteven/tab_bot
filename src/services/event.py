import json
import pandas

import src.env as env
from src.db.db import DBConnector

class Event():
    def __init__(self, event) -> None:
        self.db = DBConnector()
        self.event = event

    def log_to_db(self):
        self.db.write_to_table(env.get_events_table_name(), self.event)

