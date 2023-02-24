from state_tree.base_state import BaseState


class Four(BaseState):
    msg = """Here is the answer to question #4 👇

We do not provide mastering services
 
If you choose the "ghostwriting" service, at the end you will receive a demo track
(minimally mixed) + project stems.

    """

    def __init__(self):
        super().__init__()
        self.buttons = [("Main Menu 🎡", "menu"),
                        ("Choose a different question ↩️", "questions")]

    def process(self, txt='', mark=bool) -> 'BaseState':
        if txt:
            from buttons_dict import buttons_dict
            return buttons_dict[txt]()
