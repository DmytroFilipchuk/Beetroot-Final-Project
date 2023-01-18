from state_tree.base_state import BaseState


class FFeelTools(BaseState):
    msg = "Вітаю в секції FFeelTools!\N{ghost}"

    def __init__(self):
        super().__init__()
        self.buttons = [("Підібрати референси 🎵", 'reference'), ('Конвертер голосових повідомлень 🔈', 'converter'),
                        ("Назад ↩️", "back")]

    def process(self, txt='', authorized=bool) -> 'BaseState':

        if txt == 'reference':
            from state_tree.ffeel_tools.reference import Reference
            return Reference()

        if txt == 'converter':
            from state_tree.ffeel_tools.converter import Converter
            return Converter()

        if txt == "back":
            from state_tree.main_menu import Main_menu
            return Main_menu()
