from state_tree.base_state import BaseState


class Change_phone_number(BaseState):

    msg = "Enter your phone number in the following format -  +380... for authorization 📝"

    def __init__(self):
        super().__init__()
        self.buttons = [("Головне меню 🎡", "menu")]

    def process(self, txt='', mark = bool) -> "BaseState":
        from buttons_dict import buttons_dict
        if txt in buttons_dict.keys():
            return buttons_dict[txt]()




