from typing import Optional
import discord
from src.common.utils import convert_list_to_select_options
from src.enums.event_enums import TabEvents
from typing import Dict, List

class BaseSelect(discord.ui.Select):
    def __init__(self, *args, **kwargs) -> None:
        kwargs["placeholder"] = kwargs.get("placeholder", "Choose your action")
        kwargs["min_values"] = kwargs.get("min_values", 1)
        kwargs["max_values"] = kwargs.get("max_values", 1)
        kwargs["options"] = kwargs.get("options", [discord.SelectOption(label="No Options Available", value="No Value")])
        super().__init__(*args, **kwargs)
    
    async def callback(self, interaction: discord.Interaction):
        self.view.interaction_completed(interaction, self.values[0])
        self.disabled = True
        await interaction.message.edit(view=self.view)
        


class EmojiSelect(BaseSelect):
    def __init__(self, emojis: List[discord.Emoji], follow_up_item) -> None:
        super().__init__()
        _options = [
            {
                "key": emoji.name,
                "value": emoji.id,
                "emoji":f":{emoji.name}:{emoji.id}"
            }
            for emoji in emojis
        ]
        self.options = convert_list_to_select_options(_options)
        self.follow_up_item: Optional[discord.ui.View|discord.ui.Modal] = follow_up_item

    async def callback(self, interaction: discord.Interaction):
        selected = await interaction.guild.fetch_emoji(self.values[0])
        await interaction.response.send_message(content=str(selected))
        self.disabled = True
        await interaction.message.edit(view=self.view)

class TabEventSelect(BaseSelect):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        _options = [
            {
                "key": item.value, 
                "value": item.name
                }
                for item in TabEvents
        ]
        self.options = convert_list_to_select_options(_options)


class ListTabsSelect(BaseSelect):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        _options = [
            {
                "key": item.get("description"), 
                "value": item.get("tab_id"),
                "emoji": item.get("emoji")
                }
                for item in kwargs.get("tabs", [])
        ]
        self.options = convert_list_to_select_options(_options)

    async def callback(self, interaction: discord.Interaction):
        self.disabled = True
        await interaction.message.edit(view=self.view)
        return self.values[0]
    
