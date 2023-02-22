from state_tree.base_state import BaseState


class Reference(BaseState):
    msg = "Waiting for a link to the Spotify playlist from you 🎤"

    def __init__(self):
        super().__init__()
        self.buttons = [("Main Menu 🎡", "menu"), ("Back ↩️", "back")]

    def process(self, txt='', mark=bool) -> 'BaseState':
        if txt == "menu":
            from state_tree.main_menu import MainMenu
            return MainMenu()
        if txt == "back":
            from state_tree.ffeel_tools.ffeeltools import FFeelTools
            return FFeelTools()
        else:
            from state_tree.ffeel_tools.reference_tempo import Reference_tempo
            return Reference_tempo()
