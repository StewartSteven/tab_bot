import discord
from discord.ext import commands
from datetime import datetime as dt
from processors.command_processors.admin_processor import AdminProcessor, Processor

class AdminCog(commands.Cog): 
    """
    Cog for admin commands
    
    Cogs are used for organizing functionality and commands for the bot
    """

    def __init__(self, bot: discord.Bot): # this is a special method that is called when the cog is loaded
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_member_join(member: discord.Member):
        members = [
            {
                "user_id": member.id,
                "name": member.name,
                "insert_date": dt.isoformat(member.created_at)
            }
        ]
        event = {"type":"MEMBER", "sub_type": "ADD", "body": members}
        eventprocessor: Processor = AdminProcessor(event) 
        eventprocessor.process()

    @commands.Cog.listener()
    async def on_member_remove(member: discord.Member):
        members = [
            {
                "user_id": member.id,
                "name": member.name,
                "insert_date": dt.isoformat(member.created_at)
            }
        ]
        event = {"type":"MEMBER", "sub_type": "REMOVE", "body": members}
        eventprocessor: Processor = AdminProcessor(event) 
        eventprocessor.process()
    
    @commands.Cog.listener()
    async def on_ready(self):
        members = [
            {
                "user_id": member.id,
                "name": member.name,
                "insert_date": dt.isoformat(member.created_at)
            }
            for member in self.bot.get_all_members()
        ]
        event = {"type":"MEMBER", "sub_type": "REFRESH", "body": members}
        eventprocessor: Processor = AdminProcessor(event) 
        eventprocessor.process()
