from state_tree.base_state import BaseState


class AdditionalInfo(BaseState):

    msg = """Write down any additional info  🖊 """

    def __init__(self):
        super().__init__()
        self.buttons = [("Main Menu 🎡", "menu"),
                        ("Back ↩️", "back")]

    def process(self, txt='', mark = bool) -> 'BaseState':
        if txt == "menu":
            from state_tree.main_menu import MainMenu
            return MainMenu()
        if txt == "back":
            from state_tree.make_an_order.deadline import Deadline
            return Deadline()
        else:
            from state_tree.make_an_order.confirmation import ConfirmOrder
            return ConfirmOrder()



