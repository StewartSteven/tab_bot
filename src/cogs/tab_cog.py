import discord
from discord.ext import commands
from processors.gui_processors.tab_processor import InitializingTabView

class GuiTabCog(commands.Cog): 
    """
    Cog for commands for Tab Management

    GUI based 

    Cogs are used for organizing functionality and commands for the bot
    """


    def __init__(self, bot: discord.Bot): # this is a special method that is called when the cog is loaded
        self.bot = bot

    @discord.slash_command(name="tabs", description = "Initiates Tab Management process")
    async def process(self, ctx: discord.ApplicationContext):
        await ctx.respond("Select and option from the menu!", view=InitializingTabView(ctx.author), ephemeral=True)


def setup(bot: discord.Bot): # this is called by Pycord to setup the cog
    bot.add_cog(GuiTabCog(bot)) # add the cog to the bot

