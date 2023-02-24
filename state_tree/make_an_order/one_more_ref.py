from state_tree.base_state import BaseState


class One_more(BaseState):

    msg = "One more 1️⃣"

    def __init__(self):
        super().__init__()
        self.buttons = [("Main Menu 🎡", "menu")]

    def process(self, txt='', mark = bool) -> 'BaseState':
        from buttons_dict import buttons_dict
        if mark is True:
            from state_tree.make_an_order.deadline import Deadline
            return Deadline()
        if txt in buttons_dict.keys():
            return buttons_dict[txt]()
        else:
            return self



