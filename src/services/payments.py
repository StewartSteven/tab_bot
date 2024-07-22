from datetime import datetime as dt
from src.services.db import DBConnector

class PaymentService:
    def __init__(self) -> None:
        self.db_connector = DBConnector()

    def make_payment(self, event: dict):
        self.db_connector.create_payment(event=event)
        payment_status = self.db_connector.get_user_payment_status_by_tab(event)
        print(payment_status)
        self.db_connector.update_user_tab_map(payment_status)
        return payment_status

    def process_overpayment(self, payment_status: dict):
        overpayment_amount = abs(float(payment_status.get("amount_remaining")))
        _res = self.db_connector.get_user_payment_status(payment_status.get("user_id"))

        for tab in _res:
            if overpayment_amount > 0:
                amount_remaining = float(tab.get("amount_remaining"))
                if overpayment_amount >= amount_remaining:
                    _event = {
                        "tab_id": tab.get("tab_id"),
                        "user_id": tab.get("user_id"),
                        "amount": amount_remaining,
                        "date": dt.isoformat(dt.now())
                    }
                    self.make_payment(_event)
                    overpayment_amount = overpayment_amount - amount_remaining
                else:
                    _event = {
                    "tab_id": tab.get("tab_id"),
                    "user_id": tab.get("user_id"),
                    "amount": overpayment_amount,
                    "date": dt.isoformat(dt.now())
                    }
                    self.make_payment(_event)
                    overpayment_amount = 0
                    print("All old tabs have been paid off.")
                    break
                    

        if overpayment_amount > 0:
            _event = {
                "tab_id": payment_status.get("tab_id"),
                "user_id": payment_status.get("user_id"),
                "recipient_user_id": payment_status.get("recipient_user_id"),
                "amount_remaining": overpayment_amount
            }
            self.db_connector.handle_remaining_overpayment(_event)

    def process_payment_event(self, event: dict):
        payment_status = self.make_payment(event)
        if payment_status.get("over_paid"):
            self.process_overpayment(payment_status)
            
