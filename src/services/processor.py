from abc import ABC
import os, sys
import discord

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))

import src.common.utils as utils
import src.env as env
from src.db.db import DBConnector 

from gui.views import (
    CreateTabView, 
    UpdateTabView, 
    DeleteTabView, 
    GetTabView
    )

class ProcessorSelector():
    """
    Factory class to select event processor
    """
    def __init__(self, event_type: str) -> None:
        self.event_type = event_type
        
    def get_event_processor(self):
        processor = {
            "TAB": TabProcessor,
            "MEMBER": MemberProcessor
        }

        processor: Processor = processor.get(self.event_type)
        return processor

class Processor():
    """
    Event Processor base class
    """
    def __init__(self, sub_type: str, ctx: discord.ApplicationContext, event = None) -> None:
        self.sub_type = sub_type
        self.ctx = ctx
        self.db = DBConnector()
        self.event = event
        
    def _log_event(self):
        self.db.write_to_table(env.get_events_table_name(), self.event)
       
    def process(self):
        pass
    

class TabProcessor(Processor):
    """
    Tab Processor class
    """
    def __init__(self, event, ctx) -> None:
        super().__init__(event, ctx)
        
    
    def process(self):
        event_type = {
            "CREATE": self.create_tab,
            "DELETE": self.delete_tab,
            "UPDATE": self.update_tab,
            "GET": self.get_tab,
        }
        
        processor = event_type.get(self.sub_type)
        processor()

    def create_tab(self):
        view = CreateTabView()
        
        
    def delete_tab(self):
        view = DeleteTabView()
        
    def update_tab(self):
        view = UpdateTabView()
        
    def get_tab(self):
        file_list = self.db.list_files()
        tab_modal = GetTabView()
        return tab_modal


class MemberProcessor(Processor):
    """
    Member Processor class
    """
    def __init__(self, event, ctx) -> None:
        super().__init__(event, ctx)
        
    
    def process(self, event):
        event_type = {
            "ADD": self.add_member,
            "REMOVE": self.remove_member,
            "REFRESH": self.refresh_members
        }
        
        processor = event_type.get(self.sub_type)
        processor(event)

    def add_member(self):
        pass
        
    def remove_member(self):
        pass

    def refresh_members(self):
        pass
       

if __name__ == "__main__": 
    pass