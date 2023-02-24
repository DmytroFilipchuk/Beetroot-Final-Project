from state_tree.base_state import BaseState


class Settings(BaseState):
    msg = "Settings Menu 👇️"

    def __init__(self):
        super().__init__()
        self.buttons = [("Change phone number 📞", "phone_number"), ("Main Menu 🎡", "menu")]

    def process(self, txt='', mark=bool) -> 'BaseState':
        from buttons_dict import buttons_dict
        if txt in buttons_dict.keys():
            return buttons_dict[txt]()


