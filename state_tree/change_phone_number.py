from state_tree.base_state import BaseState


class Change_phone_number(BaseState):

    msg = "Напиши свій новий номер телефону у форматі +380...  📝"

    def __init__(self):
        self.buttons = [("Головне меню 🎡", "menu")]

    def process(self, txt='', authorized = bool) -> 'BaseState':
        if txt == "menu":
            from state_tree.main_menu import Main_menu
            return Main_menu()
        else:
            from state_tree.main_menu import Main_menu
            return Main_menu()



