from state_tree.base_state import BaseState


class Questions(BaseState):
    msg = """Here is a list of frequently asked questions👇
    
1. How quickly will the work be done (Record for Me / Ghostwriting)❓
2. Is it possible to arrange a "live" meeting❓
3. Is it possible to use the services of a session musician in other cities❓
4. Is track mastering included in the payment for the ghostwriting service❓
5. How is the payment made❓


Select the number of the question you are interested in 👇 
   """

    def __init__(self):
        super().__init__()
        self.buttons = [("1️⃣", 'one'),
                        ('2️⃣', 'two'),
                        ('3️⃣', 'three'),
                        ("4️⃣", "four"),
                        ("5️⃣", "five"),
                        ("Назад ↩️", "back")]

    def process(self, txt='', mark=bool) -> 'BaseState':
        if txt == "one":
            from state_tree.question_answers.one import One
            return One()

        if txt == "two":
            from state_tree.question_answers.two import Two
            return Two()

        if txt == "three":
            from state_tree.question_answers.three import Three
            return Three()

        if txt == "four":
            from state_tree.question_answers.four import Four
            return Four()

        if txt == "five":
            from state_tree.question_answers.five import Five
            return Five()

        if txt == "back":
            from state_tree.make_an_order.client import Client
            return Client()
