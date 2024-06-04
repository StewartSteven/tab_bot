class BaseDiscordEvent:
    def __init(self, message):
        self.message = message
        self.event_type = message.get("")
        
class TabEvent(BaseDiscordEvent):
    def __init__(self) -> None:
        pass