import discord
from discord.ext import commands
from discord.commands import SlashCommandGroup
from src.services.processor import Processor, ProcessorSelector, TabProcessor

class TabCog(commands.Cog): 
    """
    Cog for commands for Tab Management

    Cogs are used for organizing functionality and commands for the bot
    """

    tab_group = SlashCommandGroup("tabs", "Commands for Tab Management")

    def __init__(self, bot: discord.Bot): # this is a special method that is called when the cog is loaded
        self.bot = bot

    @tab_group.command(name="create")
    async def process_event(ctx):
        event = {"type":"TAB", "sub_type": "DELETE"}
        eventprocessor: Processor = ProcessorSelector(event["type"]).get_event_processor(event["sub_type"], ctx)
        eventprocessor.process()

    @tab_group.command(name="delete")
    async def process_event(ctx):
        event = {"type":"TAB", "sub_type": "DELETE"}
        eventprocessor: Processor = ProcessorSelector(event["type"]).get_event_processor(event["sub_type"], ctx)
        eventprocessor.process()

    @tab_group.command(name="update")
    async def process_event(ctx):
        event = {"type":"TAB", "sub_type": "UPDATE"}
        eventprocessor: Processor = ProcessorSelector(event["type"]).get_event_processor(event["sub_type"], ctx)
        eventprocessor.process()

    @tab_group.command(name="get")
    async def process_event(ctx):
        event = {"type":"TAB", "sub_type": "GET"}
        eventprocessor: Processor = ProcessorSelector(event["type"]).get_event_processor(event["sub_type"], ctx)
        eventprocessor.process()


def setup(bot: discord.Bot): # this is called by Pycord to setup the cog
    bot.add_cog(TabCog(bot)) # add the cog to the bot