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


class TabActionButton(DefaultButton):
    def __init__(self, label, processor=None, event=None, edit_modal = None):
        self.edit_modal: discord.ui.Modal = edit_modal
        super().__init__(label, processor, event)
    
    async def callback(self, interaction: discord.Interaction):
        view: discord.ui.View = self.view 
        if self.label.upper() == "CONFIRM":
            self.processor(self.event)
            await interaction.respond("Process Completed", ephemeral=True)
        elif self.label.upper() == "EDIT":
            await interaction.response.send_modal(self.edit_modal)
            await interaction.followup.send("Editing Prompt...", ephemeral=True)
        else:
            await interaction.respond("Canceling Process", ephemeral=True)
        await interaction.followup.delete_message(view.message.id)
