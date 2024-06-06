from dis import disco
from typing import Dict, List
import discord
import src.env as env
from src.common.utils import convert_list_to_select_options
from discord.ui.item import Item


def event_selector(event_type):
        event_types = {
            "TAB": env.TAB_EVENTS
        }
        return event_types.get(event_type)

class BaseView(discord.ui.View):

    def __init__(self, *items: Item, timeout: float | None = 180, disable_on_timeout: bool = False):
        super().__init__(*items, timeout=timeout, disable_on_timeout=disable_on_timeout)

class InitializingTabView(BaseView):

    def __init__(self, *items: Item, timeout: float | None = 180, disable_on_timeout: bool = False):
        super().__init__(*items, timeout=timeout, disable_on_timeout=disable_on_timeout)

    @discord.ui.select( # the decorator that lets you specify the properties of the select menu
        placeholder = "Choose your action", # the placeholder text that will be displayed if nothing is selected
        min_values = 1, # the minimum number of values that must be selected by the users
        max_values = 1, # the maximum number of values that can be selected by the users
        options = convert_list_to_select_options(env.TAB_EVENTS))
    async def initialize(self, select, interaction: discord.Interaction):
        event = {"type":"TAB", "sub_type": select.values[0]}
        select.disabled = True

        await interaction.response.edit_message(view=self)
        await interaction.followup.send(f"Hello, {event}")

class CreateTabView(BaseView):
    def __init__(self, *items: Item, timeout: float | None = 180, disable_on_timeout: bool = False):
        super().__init__(*items, timeout=timeout, disable_on_timeout=disable_on_timeout)

class DeleteTabView(BaseView):
    def __init__(self, *items: Item, timeout: float | None = 180, disable_on_timeout: bool = False):
        super().__init__(*items, timeout=timeout, disable_on_timeout=disable_on_timeout)

class UpdateTabView(BaseView):
    def __init__(self, *items: Item, timeout: float | None = 180, disable_on_timeout: bool = False):
        super().__init__(*items, timeout=timeout, disable_on_timeout=disable_on_timeout)

class GetTabView(BaseView):
    def __init__(self, *items: Item, timeout: float | None = 180, disable_on_timeout: bool = False):
        super().__init__(*items, timeout=timeout, disable_on_timeout=disable_on_timeout)