from state_tree.base_state import BaseState


class GetFileSession(BaseState):

    msg = "Send audio or a GuitarPro7 file 💾"

    def __init__(self):
        super().__init__()
        self.buttons = [("Main Menu 🎡", "menu"), ("Back ↩️", "back")]

    def process(self, txt='', mark = bool) -> 'BaseState':
        if txt == "menu":
            from state_tree.main_menu import MainMenu
            return MainMenu()
        if txt == "back":
            from state_tree.make_an_order.session_musician_section import SessionMusician
            return SessionMusician()
        else:
            from state_tree.make_an_order.deadline import Deadline
            return Deadline()
