from multiprocessing.managers import ListProxy
from typing import Dict, List
import discord

def convert_list_to_select_options(items: List[Dict[str, str]]) -> List[discord.SelectOption]:
    options: List[discord.SelectOption] = []
    for item in items:
        option = discord.SelectOption(label=item.get("description"), value=item.get("action"))
        options.append(option)
    return options
    
def convert_list_to_input_texts(items: List, style: discord.InputTextStyle = discord.InputTextStyle.short) -> List[discord.ui.InputText]:
    return [
          discord.ui.InputText(
                    label=item,
                    style=style
                    )
          for item in items
    ]

