import discord
from gui.view import BaseView, EmojiSelector
from gui.button import TabActionButton
from gui.modal import BaseModal
from gui.select import TabEventSelect

def get_event_processor(event_type) -> BaseModal:
        event_processors = {
            "CREATE": CreateTabModal,
            "DELETE": DeleteTabModal,
            "ADD_USER_TO_TAB": AddUserTabModal,
            "MAKE_PAYMENT": PaymentTabModal,
            "GET": GetTabModal,
            "LIST": ListTabsModal,
            "TEST": TestTabModal
        }
        return event_processors.get(event_type)

class TabProcessorView(BaseView):

    def __init__(self, author=None):
        super().__init__(author=author)
        select = TabEventSelect(
            placeholder = "Choose your action", # the placeholder text that will be displayed if nothing is selected
            min_values = 1, # the minimum number of values that must be selected by the users
            max_values = 1, # the maximum number of values that can be selected by the users
        )
        self.select = select
        select.callback = self.initialize
        self.add_item(
            select
        )
        
    async def initialize(self, interaction: discord.Interaction):
        event_type = self.select.values[0]
        
        ProcessorGui = get_event_processor(event_type)

        await interaction.response.send_modal(ProcessorGui())
        await interaction.followup.send("Generating Data Prompt...", ephemeral=True)
        await interaction.delete_original_response()

            
class TabConfirmationView(BaseView):
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
                TabActionButton(label=label, 
                             processor=self.processor, 
                             event=self.event,
                             edit_modal=self.edit_modal))

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        return True

class CreateTabModal(BaseModal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(title = "Create Tab", *args, **kwargs)
        self.modal_items = [
            {"label": "Name Of Tab"},
            {"label": "Recipient"},
            {"label": "Description (Optional)", "style": discord.InputTextStyle.paragraph, "required": False},
            {"label": "Senders", "style": discord.InputTextStyle.multiline,
            "placeholder": "Name, Amount. Senders must be newline separated"}
            ] 
        self.confirmation_view = TabConfirmationView
        self.set_items(self.modal_items)
        self.embed_fields = {
            "Name Of Tab": "Name Of Tab",
            "Recipient": "Recipient",
            "Description (Optional)": "Description",
            "Senders": "Senders"
            }

        
class AddUserTabModal(BaseModal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(title = "Update Tab", *args, **kwargs)
        self.modal_items = [
            {"label": "Adjustments", "style": discord.InputTextStyle.multiline,
            "placeholder": 
            """user, Amount. New line separated"""
               }
            ] 
        self.confirmation_view = TabConfirmationView
        self.set_items(self.modal_items)    


class PaymentTabModal(BaseModal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(title = "Update Tab", *args, **kwargs)
        self.modal_items = [
            {"label": "Tab ID", "placeholder": "Must be a valid and open tab. Use GET TAB to see available tabs."},
            {"label": "User"},
            {"label": "Amount"}
            ] 
        self.confirmation_view = TabConfirmationView
        self.set_items(self.modal_items) 


class DeleteTabModal(BaseModal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(title = "Delete Tab", *args, **kwargs)
        self.modal_items = [
            {"label": "Tab ID", "placeholder": "Must be a valid and open tab. Use GET TAB to see available tabs."}
            ] 
        self.confirmation_view = TabConfirmationView
        self.set_items(self.modal_items) 


class GetTabModal(BaseModal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(title = "Get Tab", *args, **kwargs)
        self.modal_items = [
            {"label": "Tab ID", "placeholder": "Fetches tab information."}
            ] 
        self.set_items(self.modal_items)

    async def callback(self, interaction: discord.Interaction):
        self._pre_processing()
        results: discord.Embed = self.processor(self.event)

        await interaction.response.send_message(embed=results, ephemeral=True)  
    
    def processor(self, event):
        # TODO Implement processor logic
        # Will return an embed with tab details
        _res = discord.Embed(title="Tab Information")
        return _res
    

class ListTabsModal(BaseModal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(title = "Search Criteria", *args, **kwargs)
        self.modal_items = [
            {"label": "Begin Date"},
            {"label": "End Date"},
            {"label": "Recipients", "style": discord.InputTextStyle.multiline,
            "placeholder": "Must be newline separated"},
            {"label": "Senders", "style": discord.InputTextStyle.multiline,
            "placeholder": "Must be newline separated"}
            ] 
        self.set_items(self.modal_items)

    async def callback(self, interaction: discord.Interaction):
        self.event = {item.label:item.value for item in self.children}
        results = self.processor(self.event)
        await interaction.response.send_message(embeds=[self.embed, results], ephemeral=True)  


    def processor(self, event):
        # TODO Implement processor logic
        # Will return an embed with tab details
        _res = discord.Embed(title="Tab Information")
        return _res
    
class TestTabModal(BaseModal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(title = "Create Tab", *args, **kwargs)
        self.modal_items = [
            {"label": "Test"}
            ] 
        self.confirmation_view = EmojiSelector
        self.set_items(self.modal_items)

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(view=EmojiSelector(emojis=interaction.guild.emojis))