from state_tree.base_state import BaseState


class OurServices(BaseState):
    msg = 'Перелік послуг 📌'

    def __init__(self):
        super().__init__()
        self.buttons = [("Запис партії 🎸", 'recording'),
                        ('Гоуст-райтинг 🎧', 'ghost_writer'),
                        ('Сесійний музикант  🎼  ', 'session_musician'),
                        ("Головне меню 🎡", "menu"), ("Назад ↩️", "back")]

    def process(self, txt='', mark=bool) -> 'BaseState':
        if txt == 'recording':
            from state_tree.make_an_order.recording_section import Recording
            return Recording()

        if txt == 'ghost_writer':
            from state_tree.make_an_order.ghostwriting_section import Ghostwriting
            return Ghostwriting()

        if txt == 'session_musician':
            from state_tree.make_an_order.session_musician_section import SessionMusician
            return SessionMusician()

        if txt == "menu":
            from state_tree.main_menu import MainMenu
            return MainMenu()

        if txt == "back":
            from state_tree.make_an_order.client import Client
            return Client()
