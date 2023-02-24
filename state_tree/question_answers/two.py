from state_tree.base_state import BaseState


class Two(BaseState):
    msg = """Here is the answer to question #2 👇

Yes, of course! After placing your order, a suitable meeting
can be discussed. My studio is located here ⤴️


    """

    def __init__(self):
        super().__init__()
        self.buttons = [("Main Menu 🎡", "menu"),
                        ("Choose a different question ↩️", "questions")]

    def process(self, txt='', mark=bool) -> 'BaseState':
        if txt:
            from buttons_dict import buttons_dict
            return buttons_dict[txt]()

