from state_tree.base_state import BaseState


class Questions(BaseState):
    msg = """ Ось список актуальних питань👇
    
1. Як швидко буде виконана робота (запис/трек під ключ)❓
2. Чи можна домовитись про "живу" зустріч❓
3. Чи можна скористатить послугою сесійного музиканта в інших містах❓
4. Чи входить мастеринг треку в оплату послуги "трек під ключ"❓
5. Як проходить оплата❓


Вибери номер актуального питання, яке тебе цікавить 👇    
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
