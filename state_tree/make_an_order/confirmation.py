from state_tree.base_state import BaseState


class ConfirmOrder(BaseState):

    msg = "Підтверджуєте правильність данних?  📑 "

    def __init__(self):
        super().__init__()
        self.buttons = [("Так ✅", 'yes'),
                        ('Ні ❌', 'no'),
                        ("Назад ↩️", "back")]

    def process(self, txt='', authorized = bool) -> 'BaseState':

        if txt == 'yes':
            from state_tree.make_an_order.confirmed import Confirmed
            return Confirmed()

        if txt == 'no':
            from state_tree.make_an_order.our_services import OurServices
            return OurServices()

        if txt == "back":
            from state_tree.make_an_order.additional_info import AdditionalInfo
            return AdditionalInfo()
