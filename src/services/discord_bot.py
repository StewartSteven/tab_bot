import discord
import common.env as env
from src.db.db import DBConnector 

class DiscordBot(discord.Bot):
    def __init__(self, description=None, *args, **options):
        super().__init__(description, *args, **options)
        