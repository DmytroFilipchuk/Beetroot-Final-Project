from state_tree.base_state import BaseState


class Settings(BaseState):
    msg = "Settings Menu 👇️"

    def __init__(self):
        super().__init__()
        self.buttons = [("Change phone number 📞", "phone_number"), ("Main Menu 🎡", "menu")]

    def process(self, txt='', mark=bool) -> 'BaseState':
        if txt == "phone_number":
            from state_tree.change_phone_number import Change_phone_number
            return Change_phone_number()

        if txt == "menu":
            from state_tree.main_menu import MainMenu
            return MainMenu()
