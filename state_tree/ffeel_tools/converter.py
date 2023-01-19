
from state_tree.base_state import BaseState


class Converter(BaseState):

    msg = "Чекаю на твоє голосове повідомлення 🎙"

    def __init__(self):
        super().__init__()
        self.buttons = [("Головне меню 🎡", "menu"), ("Назад ↩️", "back")]

    def process(self, txt = '', mark = bool) -> 'BaseState':
        if txt == "menu":
            from state_tree.main_menu import MainMenu
            return MainMenu()
        if txt == "back":
            from state_tree.ffeel_tools.ffeeltools import FFeelTools
            return FFeelTools()
        else:
            from state_tree.main_menu import MainMenu
            return MainMenu()


