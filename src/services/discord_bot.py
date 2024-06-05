import discord
import src.env as env
from src.db.db import DBConnector 

class DiscordBot(discord.Bot):
    def __init__(self, description=None, *args, **options):
        super().__init__(description, *args, **options)
        self.db = DBConnector()
        

    
    def _log_event(self, event):
        self.db.write_to_table(env.get_events_table_name(), event)
        
