import pandas as pd
import src.env as env   
import os

class DBConnector():
    def __init__(self) -> None:
        pass

    def list_files(self):
        file_list = [file for file in os.listdir(env.get_files_dir())]
        return file_list

    def write_to_table(self, table_name, event):
        pass
    