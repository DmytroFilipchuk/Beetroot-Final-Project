from state_tree.base_state import BaseState


class Reference(BaseState):
    msg = "Очікую посилання на Spotify плейлист від тебе 🎤"

    def __init__(self):
        super().__init__()
        self.buttons = [("Головне меню 🎡", "menu"), ("Назад ↩️", "back")]

    def process(self, txt='', authorized=bool) -> 'BaseState':
        if txt == "menu":
            from state_tree.main_menu import Main_menu
            return Main_menu()
        if txt == "back":
            from state_tree.ffeel_tools.ffeeltools import FFeelTools
            return FFeelTools()
        else:
            from state_tree.ffeel_tools.reference_tempo import Reference_tempo
            return Reference_tempo()
