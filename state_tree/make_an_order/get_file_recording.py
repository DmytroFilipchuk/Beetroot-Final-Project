from state_tree.base_state import BaseState


class GetFileRecording(BaseState):

    msg = "Надішли аудіо або GuitarPro7 файл 💾"

    def __init__(self):
        super().__init__()
        self.buttons = [("Головне меню 🎡", "menu"), ("Назад ↩️", "back")]

    def process(self, txt='', mark = bool) -> 'BaseState':
        if txt == "menu":
            from state_tree.main_menu import MainMenu
            return MainMenu()
        if txt == "back":
            from state_tree.make_an_order.recording_section import Recording
            return Recording()
        else:
            from state_tree.make_an_order.deadline import Deadline
            return Deadline()

