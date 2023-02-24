from state_tree.base_state import BaseState


class OurServices(BaseState):
    msg = 'List of services 📌'

    def __init__(self):
        super().__init__()
        self.buttons = [("Record for Me 🎸", 'recording'),
                        ('Ghostwriting 🎧', 'ghost_writer'),
                        ('Session Musician  🎼  ', 'session_musician'),
                        ("Main Menu 🎡", "menu"), ("Back ↩️", "back")]

    def process(self, txt='', mark=bool) -> 'BaseState':
        from buttons_dict import buttons_dict
        if txt in buttons_dict.keys():
            return buttons_dict[txt]()
        if txt == "back":
            from state_tree.make_an_order.client import Client
            return Client()





