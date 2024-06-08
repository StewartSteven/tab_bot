import discord

class DefaultButton(discord.ui.Button):
    def __init__(self, label, processor = None, event = None):
        super().__init__(label=label)
        self.processor = processor
        self.event = event
    
    async def callback(self, interaction: discord.Interaction):
        _res = self.processor(self.event)
        message = f"Event Failed: {_res}" if not _res else f"Event Succeeded"
        await interaction.respond(message, ephemeral=True)

