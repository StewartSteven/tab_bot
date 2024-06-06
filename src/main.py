import os, sys
import discord
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))

from src.services.discord_bot import DiscordBot
from src.cogs.tab_cog import TabCog
from src.cogs.members_cog import MembersCog
import src.env as env



bot = DiscordBot()
bot.add_cog(TabCog(bot=bot))
# bot.add_cog(MembersCog(bot=bot))

bot.run(env.get_token())