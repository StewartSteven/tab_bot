from typing import List
import discord

def convert_list_to_select_options(items: List) -> List[discord.SelectOption]:
    options: List[discord.SelectOption] = []
    for item in items:
        option = discord.SelectOption(label=item, value=item)
        options.append(option)
    return options