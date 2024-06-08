import discord

class BaseView(discord.ui.View):
    def __init__(self, author=None):
        self.author = author
        super().__init__()
    
    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        return interaction.user.id == self.author.id
    
    async def on_check_failure(self, interaction: discord.Interaction) -> None:
        await interaction.respond(f"Only the caller can use this command at the moment")
