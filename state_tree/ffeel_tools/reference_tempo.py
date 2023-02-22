from state_tree.base_state import BaseState


class Reference_tempo(BaseState):
    msg = "Enter the tempo 🔢"

    def __init__(self):
        super().__init__()
        self.buttons = [("Main Menu 🎡", "menu"), ("Back ↩️", "back")]

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
