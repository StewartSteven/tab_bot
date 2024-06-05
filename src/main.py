import os
import discord
from src.services.discord_bot import DiscordBot
from src.cogs.tab_cog import TabCog
from src.cogs.members_cog import MembersCog

import src.env as env

bot = DiscordBot(intents=discord.Intents.all())

bot.add_cog(TabCog(bot=bot))
bot.add_cog(MembersCog(bot=bot))

bot.run(env.get_token())