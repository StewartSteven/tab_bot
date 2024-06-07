import discord
import common.env as env
from src.common.utils import convert_list_to_select_options
from gui.tab_modals import (
    BaseModal, 
    CreateTabModal, 
    DeleteTabModal, 
    AddUserTabModal,
    PaymentTabModal, 
    GetTabModal
    )

class GuiProcessorSelector():
    """
    Factory class to select event processor
    """  
    def get_event_processor(self, event_type):
        processor = {
            "CREATE": CreateTabModal,
            "DELETE": DeleteTabModal,
            "ADD_USER_TO_TAB": AddUserTabModal,
            "MAKE_PAYMENT": PaymentTabModal,
            "GET": GetTabModal
        }

        processor: BaseModal = processor.get(event_type)
        return processor

class BaseView(discord.ui.View):

    def __init__(self, author):
        self.author = author
        super().__init__()
    
    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        return interaction.user.id == self.author.id
    
    async def on_check_failure(self, interaction: discord.Interaction) -> None:
        await interaction.respond(f"Only the caller can use this command at the moment")

class InitializingTabView(BaseView):

    def __init__(self, author):
        super().__init__(author=author)

    @discord.ui.select( # the decorator that lets you specify the properties of the select menu
        placeholder = "Choose your action", # the placeholder text that will be displayed if nothing is selected
        min_values = 1, # the minimum number of values that must be selected by the users
        max_values = 1, # the maximum number of values that can be selected by the users
        options = convert_list_to_select_options(env.TAB_EVENTS))
    async def initialize(self, select, interaction: discord.Interaction):
        event_type = select.values[0]
        
        GuiSelector = GuiProcessorSelector()
        ProcessorGui = GuiSelector.get_event_processor(event_type)

        await interaction.response.send_modal(ProcessorGui())
        await interaction.followup.send("Generating Data Prompt...", ephemeral=True)
        await self.wait()
                
        select.disabled = True
        await interaction.edit_original_response(view=self)

