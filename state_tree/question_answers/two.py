from state_tree.base_state import BaseState


class Two(BaseState):
    msg = """Ось відповідь на питання №2 👇

Так, звісно! Після оформлення Твого замовлення відповідну зустріч
можна буде обговорити. Моя студія знаходиться ось тут ⤴️

    """

    def __init__(self):
        super().__init__()
        self.buttons = [("Головне меню 🎡", "menu"),
                        ("Назад до списку ↩️", "questions")]

    def process(self, txt='', mark=bool) -> 'BaseState':
        if txt == "menu":
            from state_tree.main_menu import MainMenu
            return MainMenu()

        if txt == 'questions':
            from state_tree.make_an_order.question_list import Questions
            return Questions()
