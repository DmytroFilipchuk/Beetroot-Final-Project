from state_tree.base_state import BaseState


class AdditionalInfo(BaseState):

    msg = """Write down any additional info  🖊 """

    def __init__(self):
        super().__init__()
        self.buttons = [("Main Menu 🎡", "menu"),
                        ("Back ↩️", "back")]

    def process(self, txt='', mark = bool) -> 'BaseState':
        from buttons_dict import buttons_dict
        if txt in buttons_dict.keys():
            return buttons_dict[txt]()
        if txt == "back":
            from state_tree.make_an_order.deadline import Deadline
            return Deadline()
        else:
            from state_tree.make_an_order.confirmation import ConfirmOrder
            return ConfirmOrder()



