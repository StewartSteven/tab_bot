class DiscordEvent:
    """
    Class representing an input event from Discord
    """
    def __init__(self, message):
        self.message = message
        self.type = message.get("type")
        self.sub_type = message.get("sub_type")
        self.body = message.get("body")
    
