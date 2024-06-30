import discord
from src.gui.select import EmojiSelect

class BaseView(discord.ui.View):
    def __init__(self, author=None):
        self.author = author
        super().__init__()
    
    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if self.author:
            return interaction.user.id == self.author.id
        else:
            return True
    
    async def on_check_failure(self, interaction: discord.Interaction) -> None:
        await interaction.respond(f"Only the caller can use this command at the moment")

class EmojiSelector(BaseView):
    def __init__(self, emojis, follow_up_item = None, author=None):
        super().__init__(author)
        self.select = EmojiSelect(emojis=emojis, follow_up_item = follow_up_item)
        self.add_item(self.select)
