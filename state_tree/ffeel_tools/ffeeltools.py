from state_tree.base_state import BaseState


class FFeelTools(BaseState):
    msg = "Welcome to the FFeelTools section!\N{ghost}"

    def __init__(self):
        super().__init__()
        self.buttons = [("Filter playlist by tempo đĩ", 'reference'), ('Converter of voice messages đ', 'converter'),
                        ("Back âŠī¸", "back")]

    def process(self, txt='', mark=bool) -> 'BaseState':
        from buttons_dict import buttons_dict
        if txt in buttons_dict.keys():
            return buttons_dict[txt]()

        if txt == "back":
            from state_tree.main_menu import MainMenu
            return MainMenu()
