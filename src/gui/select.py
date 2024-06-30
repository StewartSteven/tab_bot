from typing import Optional
import discord
from src.common.utils import convert_enum_to_select_options, convert_emojis_to_select_options
from src.enums.event_enums import TabEvents

class BaseSelect(discord.ui.Select):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class EmojiSelect(BaseSelect):
    def __init__(self, emojis, follow_up_item) -> None:
        super().__init__()
        self.options = convert_emojis_to_select_options(emojis)
        self.follow_up_item: Optional[discord.ui.View|discord.ui.Modal] = follow_up_item

    async def callback(self, interaction: discord.Interaction):
        selected = await interaction.guild.fetch_emoji(self.values[0])
        await interaction.response.send_message(content=str(selected))
        self.disabled = True
        await interaction.message.edit(view=self.view)

class TabEventSelect(BaseSelect):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.options = convert_enum_to_select_options(TabEvents)
