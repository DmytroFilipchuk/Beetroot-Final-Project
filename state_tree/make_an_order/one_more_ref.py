from state_tree.base_state import BaseState


class One_more(BaseState):

    msg = "Ще один 1️⃣"

    def __init__(self):
        super().__init__()
        self.buttons = [("Головне меню 🎡", "menu")]

    def process(self, txt='', mark = bool) -> 'BaseState':

        if txt == "menu":
            from state_tree.main_menu import MainMenu
            return MainMenu()

        elif mark is True:
            from state_tree.make_an_order.deadline import Deadline
            return Deadline()

        else:
            return self



