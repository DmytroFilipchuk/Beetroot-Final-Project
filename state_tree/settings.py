from state_tree.base_state import BaseState


class Settings(BaseState):
    msg = "Меню налаштувань👇️"

    def __init__(self):
        super().__init__()
        self.buttons = [("Змінити номер телефону 📞", "phone_number"), ("Головне меню 🎡", "menu")]

    def process(self, txt='', authorized=bool) -> 'BaseState':
        if txt == "phone_number":
            from state_tree.change_phone_number import Change_phone_number
            return Change_phone_number()

        if txt == "menu":
            from state_tree.main_menu import Main_menu
            return Main_menu()
