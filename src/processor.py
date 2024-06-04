# from src.services.tab import tab 
# from src.model.event import TabEvent

class EventProcessor():
    def __init__(self, event) -> None:
        self.event = event
        
    def get_processor(self):
        processor = {
            "TAB": TabProcessor,
            "PLACEHOLDER": None
        }

        processor: EventProcessor = processor.get(self.event.get("type"))
        return processor(self.event)
    
    def process(self):
        """
        process
        """
        pass

class TabProcessor(EventProcessor):
    def __init__(self, event) -> None:
        self.event = event
        
    
    def process(self):
        event_type = {
            "CREATE": self.create,
            "DELETE": self.delete,
            "UPDATE": self.update,
            "GET": self.get,
        }
        
        processor = event_type.get(self.event.get("sub_type"))
        processor()
        
    def create(self):
        print("create")
            
    def delete(self):
        print("delete")
            
    def update(self):
        print("update")
            
    def get(self):
        print("get")


if __name__ == "__main__": 
    eventprocessor = EventProcessor({"type":"TAB", "sub_type": "DELETE"})
    processor: TabProcessor = eventprocessor.get_processor()

    processor.process()