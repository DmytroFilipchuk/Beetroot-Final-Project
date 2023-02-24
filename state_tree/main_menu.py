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
        from buttons_dict import buttons_dict
        if txt in buttons_dict.keys():
            return buttons_dict[txt]()


