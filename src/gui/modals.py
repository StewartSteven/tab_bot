from ast import Pass
from typing import List
import discord

class BaseModal(discord.ui.modal): 
    """
    Class representing Dicord Modals

    """
    def __init__(self, *args, **kwargs) -> None:
        super.__init__(*args, **kwargs)

    def set_items():
        pass
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
   