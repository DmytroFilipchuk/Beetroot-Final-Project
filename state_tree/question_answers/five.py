from state_tree.base_state import BaseState


class Five(BaseState):
    msg = """Here is the answer to question #5 👇

The first part of the payment is made after 1 min 30 sec of the song is approved.

The second half is paid upon completion of the work.

    """

    def __init__(self):
        super().__init__()
        self.buttons = [("Main Menu 🎡", "menu"),
                        ("Choose a different question ↩️", "questions")]

    def process(self, txt='', mark=bool) -> 'BaseState':
        if txt:
            from buttons_dict import buttons_dict
            return buttons_dict[txt]()
