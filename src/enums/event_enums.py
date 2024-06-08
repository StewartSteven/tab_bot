from enum import Enum

class TabEvents(Enum):
    """
    Enum for Tab Events
    """
    CREATE = "Create a new tab"
    ADD_USER_TO_TAB = "Add a user to an existing tab (by tab id)"
    MAKE_PAYMENT = "Make a payment on an existing tab"
    DELETE = "Delete an existing tab"
    GET = "Retrieve an existing tab"
    LIST = "Search for existing tabs"
