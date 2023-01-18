from state_tree.base_state import BaseState


class Main_menu(BaseState):
    msg = 'Чим я можу тобі допомогти?\N{eyes}'

    def __init__(self):
        super().__init__()
        self.buttons = [("Зробити замовлення 📀", 'client'),
                        ('FFeelTools 🎹', 'ffeeltools'),
                        ("Налаштування ⚙️", "settings"),
                        ("Про нас 🫂", "about")]

    def process(self, txt='', authorized=bool) -> 'BaseState':

        if txt == 'client':
            from state_tree.make_an_order.client import Client
            return Client()

        if txt == 'ffeeltools':
            from state_tree.ffeel_tools.ffeeltools import FFeelTools
            return FFeelTools()

        if txt == 'settings':
            from state_tree.settings import Settings
            return Settings()

        if txt == 'about':
            from state_tree.about_us import AboutUs
            return AboutUs()
