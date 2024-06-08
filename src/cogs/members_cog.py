import discord
from discord.ext import commands
from processors.command_processors.member_processor import Processor, ProcessorSelector

class MembersCog(commands.Cog): 
    """
    Cog to automate Member Updates
    
    Note: This Cog only contains commands that run on new members being added or when the bot is first ran

    Cogs are used for organizing functionality and commands for the bot
    """

    def __init__(self, bot: discord.Bot): # this is a special method that is called when the cog is loaded
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_member_join(member):
        event = {"type":"MEMBER", "sub_type": "ADD", "body": member.mention}
        eventprocessor: Processor = ProcessorSelector(event["type"]).get_event_processor(event["sub_type"], None)
        eventprocessor.process(member.mention)

    @commands.Cog.listener()
    async def on_member_remove(member):
        event = {"type":"MEMBER", "sub_type": "REMOVE", "body": member.mention}
        eventprocessor: Processor = ProcessorSelector(event["type"]).get_event_processor(event["sub_type"], None)
        eventprocessor.process(member.mention)
    
    @commands.Cog.listener()
    async def on_ready(member, ctx):
        event = {"type":"MEMBER", "sub_type": "REFRESH", "body": member.mention}
        eventprocessor: Processor = ProcessorSelector(event["type"]).get_event_processor(event["sub_type"], ctx)
        eventprocessor.process(member.mention)


def setup(bot: discord.Bot): # this is called by Pycord to setup the cog
    bot.add_cog(MembersCog(bot)) # add the cog to the bot