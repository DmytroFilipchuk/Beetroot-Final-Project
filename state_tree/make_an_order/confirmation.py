from state_tree.base_state import BaseState


class ConfirmOrder(BaseState):

    msg = "Do you confirm the accuracy of the data? 📑 "

    def __init__(self):
        super().__init__()
        self.buttons = [("Yes ✅", 'yes'),
                        ('No ❌', 'no'),
                        ("Back ↩️", "back")]

    def process(self, txt='', mark = bool) -> 'BaseState':
        from buttons_dict import buttons_dict
        if txt in buttons_dict.keys():
            return buttons_dict[txt]()
        if txt == "back":
            from state_tree.make_an_order.additional_info import AdditionalInfo
            return AdditionalInfo()
