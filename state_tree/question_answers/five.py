from state_tree.base_state import BaseState


class Five(BaseState):
    msg = """Ось відповідь на питання №5 👇

Перша частина оплати відбувається після того як одобрено 1 хв 30 сек пісні.

Друга половина платиться після завершення роботи.

    """

    def __init__(self):
        super().__init__()
        self.buttons = [("Головне меню 🎡", "menu"),
                        ("Назад до списку ↩️", "questions")]

    def process(self, txt='', authorized=bool) -> 'BaseState':
        if txt == "menu":
            from state_tree.main_menu import Main_menu
            return Main_menu()

        if txt == 'questions':
            from state_tree.make_an_order.question_list import Questions
            return Questions()