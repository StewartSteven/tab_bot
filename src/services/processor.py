from abc import ABC, abstractmethod
import os, sys
import discord
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))

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

class Processor(ABC):
    """
    Event Processor base class
    """
    def __init__(self, sub_type: str, ctx: discord.ApplicationContext, event = None) -> None:
        self.sub_type = sub_type
        self.ctx = ctx
        self.event = event

    @abstractmethod
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
        view = GetTabView()
        return view


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
            "REFRESH": self.refresh_members,
            "GET": self.get_members
        }
        
        processor = event_type.get(self.sub_type)
        processor(event)

    def add_member(self):
        pass
        
    def remove_member(self):
        pass

    def refresh_members(self):
        pass

    def get_members(self):
        pass
       

if __name__ == "__main__": 
    pass