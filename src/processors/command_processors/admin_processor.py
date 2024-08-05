from abc import ABC, abstractmethod
import os, sys
import discord
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))

from src.services.db import DBConnector

class Processor(ABC):
    """
    Event Processor base class
    """
    def __init__(self, ctx = None, event:dict = None) -> None:
        self.ctx = ctx
        self.event = event
        self.db = DBConnector()
        
    @abstractmethod
    def process(self):
        pass

class AdminProcessor(Processor):
    """
    Admin Processor class
    """
    def __init__(self, event, ctx = None) -> None:
        super().__init__(event, ctx)
    
    def process(self):
        event_type = {
            "ADD": self.add_member,
            "REMOVE": self.remove_member,
            "REFRESH": self.refresh_members,
            "GET": self.get_members
        }
        
        processor = event_type.get(self.event.get("sub_type"))
        processor()

    def add_member(self):
        """
        Use db.insert_users to add users, unsure how to pull from discord form/event
        """
        pass
        
    def remove_member(self):
        """
        Either needs to clear users and insert without removed member OR write new func in db.py
        """
        pass

    def refresh_members(self):
        self.db.clear_users()
        self.db.insert_users(self.event.get("body"))
        

    def get_members(self):
        """
        Needs new func in db.py, reference other methods and test.ipynb
        """
        pass
       

if __name__ == "__main__": 
    pass