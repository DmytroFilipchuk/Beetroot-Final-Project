from state_tree.base_state import BaseState


class Reference_tempo(BaseState):
    msg = "Вкажи потрібний темп 🔢"

    def __init__(self):
        super().__init__()
        self.buttons = [("Головне меню 🎡", "menu"), ("Назад ↩️", "back")]

    def process(self, txt='', mark=bool) -> 'BaseState':
        if txt == "menu":
            from state_tree.main_menu import MainMenu
            return MainMenu()
        if txt == "back":
            from state_tree.ffeel_tools.reference import Reference
            return Reference()
        else:
            from state_tree.main_menu import MainMenu
            return MainMenu()
