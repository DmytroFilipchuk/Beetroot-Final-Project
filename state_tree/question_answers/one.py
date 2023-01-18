from state_tree.base_state import BaseState


class One(BaseState):
    msg = """Ось відповідь на питання №1 👇
    
В залежності від обсягу та к-сті замовлень - від 3 днів до двох тижнів.
      
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
