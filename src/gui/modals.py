from typing import List
import discord

class BaseModal(discord.ui.modal): 
    """
    Class representing Dicord Modal Dialogues

    Args:
        discord (_type_): _description_
    """
    def __init__(self, *args, **kwargs) -> None:
        super.__init__(*args, **kwargs)

class CreateTabModal(BaseModal):
    def __init__(self, *args, **kwargs) -> None:
        super.__init__(*args, **kwargs)
        self.title = "Create Tab"

class UpdateTabModal(BaseModal):
    def __init__(self, *args, **kwargs) -> None:
        super.__init__(*args, **kwargs)
        self.title = "Update Tab"
  
class DeleteTabModal(BaseModal):
    def __init__(self, *args, **kwargs) -> None:
        super.__init__(*args, **kwargs)
        self.title = "Delete Tab"

class GetTabModal(BaseModal):
    def __init__(self, *args, **kwargs) -> None:
        super.__init__(*args, **kwargs)
        self.title = "Get Tab"
    async def display_tabs(options: List[discord.SelectOption]):
        pass