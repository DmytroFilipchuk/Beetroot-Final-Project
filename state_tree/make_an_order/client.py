from state_tree.base_state import BaseState


class Client(BaseState):
    msg = "Welcome to the customer section! 👨🏼‍💻"

    def __init__(self):
        super().__init__()
        self.buttons = [("List of services 🗒", 'services'),
                        ('Frequently asked questions ⁉️', 'questions'),
                        ("Back ↩️", "back")]

    def process(self, txt='', mark=bool) -> 'BaseState':
        from buttons_dict import buttons_dict
        if txt in buttons_dict.keys():
            return buttons_dict[txt]()
        if txt == "back":
            from state_tree.main_menu import MainMenu
            return MainMenu()
