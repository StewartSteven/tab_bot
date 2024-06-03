import discord
import os # default module
from dotenv import load_dotenv

load_dotenv() # load all the variables from the env file
bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.slash_command(name="hello", description="Say hello to the bot")
async def hello(ctx: discord.ApplicationContext):
    await ctx.respond("Hello!")

@bot.slash_command(name="testtesttest", description="testing")
async def testcommand(ctx: discord.ApplicationContext):
    await ctx.respond("Did It Work?")

bot.run(os.getenv('TOKEN')) # run the bot with the token