from typing import Dict, List
import discord
from src.services.db import DBConnector   
from src.common.utils import  remap_dictionary_keys

class BaseModal(discord.ui.Modal): 
    """
    Class representing Discord Modals

    For each event, a separate processor method must be created
    """
    def __init__(self, embed_fields = [], confirmation_view = None, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.db = DBConnector()
        self.embed_fields = embed_fields
        self.confirmation_view = confirmation_view
        self.event = None
        self.embed = None

    def set_items(self, items: List[Dict]):
        for item in items:
            self.add_item(
                discord.ui.InputText(
                    label=item.get("label"),
                    style=item.get("style", discord.InputTextStyle.short),
                    placeholder=item.get("placeholder"),
                    required=item.get("required", True))
                )
    


    def set_embed_fields(self, embed: discord.Embed):
        
        items = self.children if not self.embed_fields \
            else remap_dictionary_keys(self.embed_fields, self.event, convert_to_input_text=True)
        for item in items:
            embed.add_field(name=item.label, value=item.value, inline=False)
        return 
    
    def get_embed_title(self):
        embed_title = self.event.pop("Name Of Tab", self.title)
        return embed_title

    def _pre_processing(self):
        """
        Generates the event and confirmation embed.

        Should be called first in the callback function for every object that inherets this class
        """
        self.event = {item.label:item.value for item in self.children}
        embed_title = self.get_embed_title()
        self.embed = discord.Embed(title=embed_title, description="Please confirm the following")
        self.set_embed_fields(embed=self.embed)

    async def callback(self, interaction: discord.Interaction):
        self._pre_processing()
        view =  self.confirmation_view(self.processor, 
                                 event=self.event, 
                                 button_labels=["CONFIRM", "EDIT", "CANCEL"],
                                 edit_modal=self)
        await interaction.response.send_message(view=view, embed=self.embed, ephemeral=True)  

    def processor(self, event):
        """
        Event processor for the modal

        Should be overridden to handle different events by every object that inherets this class
        """
        pass    