from state_tree.base_state import BaseState


class FFeelTools(BaseState):
    msg = "Welcome to the FFeelTools section!\N{ghost}"

    def __init__(self):
        super().__init__()
        self.buttons = [("Filter playlist by tempo 🎵", 'reference'), ('Converter of voice messages 🔈', 'converter'),
                        ("Назад ↩️", "back")]

    def process(self, txt='', mark=bool) -> 'BaseState':

        if txt == 'reference':
            from state_tree.ffeel_tools.reference import Reference
            return Reference()

        if txt == 'converter':
            from state_tree.ffeel_tools.converter import Converter
            return Converter()

        if txt == "back":
            from state_tree.main_menu import MainMenu
            return MainMenu()
