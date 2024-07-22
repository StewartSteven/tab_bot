import discord
from src.gui.select import EmojiSelect
from src.services.db import DBConnector

class BaseView(discord.ui.View):
    def __init__(self, author=None):
        self.author = author
        self.db = DBConnector()
        super().__init__()
    
    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if self.author:
            return interaction.user.id == self.author.id
        return True
    
    async def on_check_failure(self, interaction: discord.Interaction) -> None:
        await interaction.respond(f"Only the caller can use this command at the moment")
    
    async def interaction_completed(self, interaction: discord.Interaction, values):
        await interaction.respond(f"Testing {values}", ephemeral=True)

class EmojiSelector(BaseView):
    def __init__(self, emojis, follow_up_item = None, author=None):
        super().__init__(author)
        self.select = EmojiSelect(emojis=emojis, follow_up_item = follow_up_item)
        self.add_item(self.select)

class TabSelector(BaseView):
    def __init__(self, user_id, author=None):
        super().__init__()
    
    def get_user_tabs(self):
        pass