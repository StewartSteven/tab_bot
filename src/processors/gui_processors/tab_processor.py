import discord
from gui.view import BaseView, EmojiSelector
from gui.button import TabActionButton
from gui.modal import BaseModal
from gui.select import TabEventSelect, ListTabsSelect, BaseSelect

def get_event_processor(event_type) -> BaseModal | BaseView:
        event_processors = {
            "CREATE": CreateTabModal,
            "DELETE": DeleteTabModal,
            "ADD_USER_TO_TAB": AddUserTabModal,
            "MAKE_PAYMENT": PaymentTabView,
            "GET": GetTabModal,
            "LIST": ListTabsModal,
            "TEST": TestEvent
        }
        return event_processors.get(event_type)

class TabProcessorView(BaseView):

    def __init__(self, author=None):
        super().__init__(author=author)
        self.select = TabEventSelect()
        self.select.callback = self.initialize
        self.add_item(
            self.select
        )
        
    async def initialize(self, interaction: discord.Interaction):
        event_type = self.select.values[0]
        
        ProcessorGui = get_event_processor(event_type)

        if issubclass(ProcessorGui, BaseModal):
            await interaction.response.send_modal(ProcessorGui())
        else:
            await interaction.respond(view=ProcessorGui(), ephemeral=True)
        
        self.select.disabled = True
        await interaction.edit(view=self)

            
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
        # TODO: Amount owed should be defaulted to default split percentage

        
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


class PaymentTabView(BaseView):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(title = "Update Tab", *args, **kwargs)
        self.select = ListTabsSelect
        # Bring up a modal with tab details
            # Inputs
                # payment amount - default value = exact amount owed 
                #   
        

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
        self.event = {item.label:item.value for item in self.children}
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
    
class TestEvent(BaseView):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__( *args, **kwargs)
        self.add_item(BaseSelect())
        