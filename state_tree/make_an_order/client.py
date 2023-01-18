from state_tree.base_state import BaseState


class Client(BaseState):
    msg = "Вітаю в секції клієнта! 👨🏼‍💻"

    def __init__(self):
        super().__init__()
        self.buttons = [("Cписок послуг 🗒", 'services'),
                        ('Популярні питання ⁉️', 'questions'),
                        ("Назад ↩️", "back")]

    def process(self, txt='', authorized=bool) -> 'BaseState':
        if txt == 'services':
            from state_tree.make_an_order.our_services import OurServices
            return OurServices()

        if txt == 'questions':
            from state_tree.make_an_order.question_list import Questions
            return Questions()

        if txt == "back":
            from state_tree.main_menu import Main_menu
            return Main_menu()
