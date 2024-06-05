import discord
import os
from src.services.discord_bot import DiscordBot
from src.model.event import DiscordEvent
from src.services.processor import Processor, ProcessorSelector, TabProcessor
bot = DiscordBot()

@bot.slash_command(name="tab")
async def send_modal(ctx):
    event = DiscordEvent({"type":"TAB", "sub_type": "DELETE"})
    eventprocessor: Processor = ProcessorSelector(event.type).get_event_processor(event)

    await eventprocessor.process()

bot.run(os.getenv('TOKEN'))