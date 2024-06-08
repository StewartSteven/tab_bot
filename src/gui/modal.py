from typing import Dict, List
import discord
from src.db.db import DBConnector   
from src.common.utils import convert_list_to_input_texts

class BaseModal(discord.ui.Modal): 
    """
    Class representing Discord Modals

    For each event, a separate processor method must be created
    """
    def __init__(self, embed_fields = [], *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.db = DBConnector()
        self.embed_fields = convert_list_to_input_texts(embed_fields, discord.InputTextStyle.multiline)
        self.event = None
        self.embed = None

    def set_items(self, items: List[Dict]):
        for item in items:
            self.add_item(
                discord.ui.InputText(
                    label=item.get("label"),
                    style=item.get("style", discord.InputTextStyle.short),
                    placeholder=item.get("placeholder"))
                )
    
    def set_embed_fields(self, embed: discord.Embed):
        items = self.children + self.embed_fields
        for item in items:
            embed.add_field(name=item.label, value=item.value)
        return 
    
    def _pre_processing(self):
        """
        Generates the event and confirmation embed.

        Should be called first in the callback function for every object that inherets this class
        """
        self.event = {item.label:item.value for item in self.children}
        self.embed = discord.Embed(title=self.title, description="Please confirm the following")
        self.set_embed_fields(embed=self.embed)
    
    def processor(self, event):
        pass    