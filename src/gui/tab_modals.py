from typing import Dict, List
import discord
from src.db.db import DBConnector   

class DefaultButton(discord.ui.Button):
    def __init__(self, label):
        super().__init__(label=label)
    
    async def callback(self, interaction: discord.Interaction):
        await interaction.respond(self.label, ephemeral=True)

class ConfirmationView(discord.ui.View):
    def __init__(self, processor, event):
        super().__init__()
        self.processor = processor
        self.event = event
        self.add_item(DefaultButton("Confirm"))
        self.add_item(DefaultButton("Edit"))
        self.add_item(DefaultButton("Cancel"))


class BaseModal(discord.ui.Modal): 
    """
    Class representing Discord Modals

    For each event, a separate processor method must be created
    """
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.db = DBConnector()

    def set_items(self, items: List[Dict]):
        for item in items:
            self.add_item(
                discord.ui.InputText(
                    label=item.get("label"),
                    style=item.get("style", discord.InputTextStyle.short),
                    placeholder=item.get("placeholder"))
                )
    
    def set_embed_fields(self, embed: discord.Embed):
        for item in self.children:
            embed.add_field(name=item.label, value=item.value)
        return 
    
    def processor(self, event):
        return True
    
    async def callback(self, interaction: discord.Interaction):
        event = {item.label:item.value for item in self.children}
        # Run event processor
        success = self.processor(event)
        status = "SUCCESS" if success else "FAILED"
        embed = discord.Embed(title=self.title, description=status)
        self.set_embed_fields(embed=embed)

        await interaction.response.send_message(embed=embed, ephemeral=True) 
        view =  ConfirmationView(self.processor, event=event)
        await interaction.followup.send(view=view, ephemeral=True)
        

class CreateTabModal(BaseModal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(title = "Create Tab", *args, **kwargs)
        self.modal_items = [
            {"label": "Debtee"},
            {"label": "Amount"},
            {"label": "Description", "style": discord.InputTextStyle.paragraph},
            {"label": "Members", "style": discord.InputTextStyle.multiline,
            "placeholder": "Names must be either new line or comma separated"}
            ] 
        self.set_items(self.modal_items)

        
class AddUserTabModal(BaseModal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(title = "Update Tab", *args, **kwargs)
        self.modal_items = [
            {"label": "Adjustments", "style": discord.InputTextStyle.multiline,
            "placeholder": 
            """user, percentage. New line separated"""
               }
            ] 
        self.set_items(self.modal_items)

class PaymentTabModal(BaseModal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(title = "Update Tab", *args, **kwargs)
        self.modal_items = [
            {"label": "Tab ID", "placeholder": "Must be a valid and open tab. Use GET TAB to see available tabs."},
            {"label": "User"},
            {"label": "Amount"}
            ] 
        self.set_items(self.modal_items)

class DeleteTabModal(BaseModal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(title = "Delete Tab", *args, **kwargs)
        self.modal_items = [
            {"label": "Tab ID", "placeholder": "Must be a valid and open tab. Use GET TAB to see available tabs."}
            ] 
        self.set_items(self.modal_items)

class GetTabModal(BaseModal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(title = "Get Tab", *args, **kwargs)
        self.modal_items = [
            {"label": "Tab ID", "placeholder": "Must be a valid and open tab. Use GET TAB to see available tabs."}
            ] 
        self.set_items(self.modal_items)
   