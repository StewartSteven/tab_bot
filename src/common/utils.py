from typing import Dict, List
import discord

def convert_list_to_select_options(items: List[Dict[str, str]]) -> List[discord.SelectOption]:
    options: List[discord.SelectOption] = []
    for item in items:
        option = discord.SelectOption(label=item.get("description"), value=item.get("action"))
        options.append(option)
    return options
    

