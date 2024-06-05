from abc import ABC
import os, sys
import discord

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))

from src.model.event import DiscordEvent
import src.common.utils as utils
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
    def __init__(self, event_type) -> None:
        self.event_type = event_type
        
    def get_event_processor(self, event: dict):
        processor = {
            "TAB": TabProcessor
        }

        processor: Processor = processor.get(self.event_type)
        return processor(event)

class Processor():
    """
    Event Processor base class
    """
    def __init__(self, event: DiscordEvent, ctx: discord.ApplicationContext) -> None:
        self.event = event
        self.ctx = ctx
    
    def process(self):
        pass
    

class TabProcessor(Processor):
    """
    Tab Processor class

    Args:
        Processor (_type_): _description_
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
        
        processor = event_type.get(self.event.sub_type)
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
    

if __name__ == "__main__": 
    pass