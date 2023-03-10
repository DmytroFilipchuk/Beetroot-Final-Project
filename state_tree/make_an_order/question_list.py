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
        from buttons_dict import buttons_dict

        if txt in buttons_dict.keys():
            return buttons_dict[txt]()
        if txt == "back":
            from state_tree.make_an_order.client import Client
            return Client()



