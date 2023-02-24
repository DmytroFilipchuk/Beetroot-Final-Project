from state_tree.base_state import BaseState


class One(BaseState):
    msg = """Here is the answer to question #1 👇.
    
Depending on the amount of work and the number of orders - from 3 days to two weeks.
      
    """

    def __init__(self):
        super().__init__()
        self.buttons = [("Main Menu 🎡", "menu"),
                        ("Choose a different question ↩️", "questions")]

    def process(self, txt='', mark=bool) -> 'BaseState':
        if txt:
            from buttons_dict import buttons_dict
            return buttons_dict[txt]()

