def event_handler(event):
    events = {
        "GET_TAB": get_event,
        "DELETE_TAB": delete_event
    }
    return events.get(event)

def get_event(val):
    print(f"GET_EVENT {val}")
def delete_event(val):
    print(f"DELETE_EVENT {val}")

event = event_handler("DELETE_TAB")

event("Steve")
