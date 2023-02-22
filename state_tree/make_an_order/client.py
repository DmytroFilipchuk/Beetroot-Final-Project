from state_tree.base_state import BaseState


class Client(BaseState):
    msg = "Welcome to the customer section! 👨🏼‍💻"

    def __init__(self):
        super().__init__()
        self.buttons = [("List of services 🗒", 'services'),
                        ('Frequently asked questions ⁉️', 'questions'),
                        ("Back ↩️", "back")]

    def process(self, txt='', mark=bool) -> 'BaseState':
        if txt == 'services':
            from state_tree.make_an_order.our_services import OurServices
            return OurServices()

        if txt == 'questions':
            from state_tree.make_an_order.question_list import Questions
            return Questions()

        if txt == "back":
            from state_tree.main_menu import MainMenu
            return MainMenu()
