import discord
import src.common.env as env
from src.common.utils import convert_list_to_select_options
from gui.view import BaseView
from gui.button import DefaultButton
from gui.modal import BaseModal

def get_event_processor(event_type) -> BaseModal:
        event_processors = {
            "CREATE": CreateTabModal,
            "DELETE": DeleteTabModal,
            "ADD_USER_TO_TAB": AddUserTabModal,
            "MAKE_PAYMENT": PaymentTabModal,
            "GET": GetTabModal
        }
        return event_processors.get(event_type)

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
        
        ProcessorGui = get_event_processor(event_type)

        await interaction.response.send_modal(ProcessorGui())
        await interaction.followup.send("Generating Data Prompt...", ephemeral=True)
        await interaction.delete_original_response()

class ActionButton(DefaultButton):
    def __init__(self, label, processor=None, event=None, edit_modal = None):
        self.edit_modal: BaseModal = edit_modal
        super().__init__(label, processor, event)
    
    async def callback(self, interaction: discord.Interaction):
        if self.label == "CONFIRM":
            self.processor(self.event())
        elif self.label == "EDIT":
            await interaction.response.send_modal(self.edit_modal)
            await interaction.followup.send("Editing Prompt...", ephemeral=True)
            await interaction.delete_original_response()
        else:
            await interaction.respond("Canceling", ephemeral=True)

            
class ConfirmationView(BaseView):
    def __init__(self, processor, event, button_labels=[], edit_modal = None):
        super().__init__()
        self.processor = processor
        self.event = event
        self.button_labels = button_labels
        self.edit_modal: BaseModal = edit_modal
        self.set_buttons()
        self.buttons_disabled = False
        
    def set_buttons(self):
        for label in self.button_labels:
            self.add_item(
                ActionButton(label=label, 
                             processor=self.processor, 
                             event=self.event,
                             edit_modal=self.edit_modal))

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        return True


class CreateTabModal(BaseModal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(title = "Create Tab", *args, **kwargs)
        self.modal_items = [
            {"label": "Recepient"},
            {"label": "Amount"},
            {"label": "Description", "style": discord.InputTextStyle.paragraph},
            {"label": "Members", "style": discord.InputTextStyle.multiline,
            "placeholder": "Names must be either new line or comma separated"}
            ] 
        self.set_items(self.modal_items)

    
    async def callback(self, interaction: discord.Interaction):
        self._pre_processing()
        view =  ConfirmationView(self.processor, 
                                 event=self.event, 
                                 button_labels=["CONFIRM", "EDIT", "CANCEL"],
                                 edit_modal=self)
        await interaction.response.send_message(view=view, embed=self.embed, ephemeral=True)  


        
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
   