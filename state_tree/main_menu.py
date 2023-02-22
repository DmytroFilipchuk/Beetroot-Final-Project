from state_tree.base_state import BaseState


class MainMenu(BaseState):
    msg = 'How can I help you?\N{eyes}'

    def __init__(self):
        super().__init__()
        self.buttons = [("Place an order 📀", 'client'),
                        ('FFeelTools 🎹', 'ffeeltools'),
                        ("Settings ⚙️", "settings"),
                        ("About Us 🫂", "about")]

    def process(self, txt='', mark=bool) -> 'BaseState':

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
