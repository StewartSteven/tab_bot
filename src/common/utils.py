from ast import Tuple
import copy
from enum import Enum
from typing import Dict, List
import discord

def convert_enum_to_select_options(items: Enum) -> List[discord.SelectOption]:
    options: List[discord.SelectOption] = []
    for item in items:
        option = discord.SelectOption(label=item.value, value=item.name)
        options.append(option)
    return options

def convert_emojis_to_select_options(items: List[discord.Emoji]) -> List[discord.SelectOption]:
    options: List[discord.SelectOption] = []
    for item in items:
        emoji_val = f":{item.name}:{item.id}"
        option = discord.SelectOption(label=item.name, value=str(item.id), emoji=emoji_val)
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

def remap_dictionary_keys(mapping_dict: Dict, value_dict: Dict, convert_to_input_text = False) -> List:
    _res = []
    v_dict = copy.deepcopy(value_dict)
    for k, v in v_dict.items():
        new_key = mapping_dict.get(k)
        if new_key:
            _res.append({
                "label": new_key,
                "value": v
            })

    if convert_to_input_text:
        _res = [
            discord.ui.InputText(
                    label=item["label"],
                    value=item["value"]
                    )
          for item in _res
        ]
    return _res
