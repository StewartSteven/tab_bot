import discord
import src.env as env
from discord.ext import commands
from discord.commands import SlashCommandGroup
from src.services.processor import Processor, ProcessorSelector, TabProcessor
from src.gui.views import InitializingTabView
from src.common.utils import convert_list_to_select_options

class TabCog(commands.Cog): 
    """
    Cog for commands for Tab Management

    Cogs are used for organizing functionality and commands for the bot
    """

    # tab_group = SlashCommandGroup("tabs", "Commands for Tab Management")

    def __init__(self, bot: discord.Bot): # this is a special method that is called when the cog is loaded
        self.bot = bot

    @discord.slash_command(name="tab")
    async def process(self, ctx):
        await ctx.respond("Select and option from the menu!", view=InitializingTabView())


def setup(bot: discord.Bot): # this is called by Pycord to setup the cog
    bot.add_cog(TabCog(bot)) # add the cog to the bot