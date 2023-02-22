from state_tree.base_state import BaseState


class ConfirmOrder(BaseState):

    msg = "Do you confirm the accuracy of the data? 📑 "

    def __init__(self):
        super().__init__()
        self.buttons = [("Yes ✅", 'yes'),
                        ('No ❌', 'no'),
                        ("Back ↩️", "back")]

    def process(self, txt='', mark = bool) -> 'BaseState':

        if txt == 'yes':
            from state_tree.make_an_order.confirmed import Confirmed
            return Confirmed()

        if txt == 'no':
            from state_tree.make_an_order.our_services import OurServices
            return OurServices()

        if txt == "back":
            from state_tree.make_an_order.additional_info import AdditionalInfo
            return AdditionalInfo()
