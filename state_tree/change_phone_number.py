from state_tree.base_state import BaseState


class Change_phone_number(BaseState):

    msg = "Напиши свій новий номер телефону у форматі +380...  📝"

    def __init__(self):
        super().__init__()
        self.buttons = [("Головне меню 🎡", "menu")]

    def process(self, txt='', mark = bool) -> "BaseState":
        if txt == "menu":
            from state_tree.main_menu import MainMenu
            return MainMenu()
        else:
            from state_tree.main_menu import MainMenu
            return MainMenu()



