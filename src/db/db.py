import pandas as pd
import src.env as env   
import os

class DBConnector():
    def __init__(self) -> None:
        pass

    def get_tab(tab_id, file_name):
        tab = pd.read_csv(file_name)
        filtered_tab = tab[tab["id"] == tab_id]

        # Perform some transformation...
        return filtered_tab

    def list_files(self):
        file_list = [file for file in os.listdir(env.get_files_dir())]
        return file_list

    def write_to_table(self, table_name, event):
        pass

    def get_payments_by_user():
        pass
    