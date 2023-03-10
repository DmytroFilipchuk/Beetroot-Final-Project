from state_tree.base_state import BaseState


class Three(BaseState):
    msg = """ Here is the answer to question #3 đ

Yes, this is possible, provided that the travel costs are covered.

    """

    def __init__(self):
        super().__init__()
        self.buttons = [("Main Menu đĄ", "menu"),
                        ("Choose a different question âŠī¸", "questions")]

    def process(self, txt='', mark=bool) -> 'BaseState':
        if txt:
            from buttons_dict import buttons_dict
            return buttons_dict[txt]()
