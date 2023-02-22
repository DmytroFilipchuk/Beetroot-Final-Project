from state_tree.base_state import BaseState


class Recording(BaseState):
    msg = "Let's get to know each other! " \
          "Enter the name of the band/performer✏️"

    def __init__(self):
        super().__init__()
        self.buttons = [("Main Menu 🎡", "menu"), ("Back ↩️", "back")]

    def process(self, txt='', mark=bool) -> 'BaseState':

        if txt == "menu":
            from state_tree.main_menu import MainMenu
            return MainMenu()

        if txt == "back":
            from state_tree.make_an_order.our_services import OurServices
            return OurServices()

        else:
            from state_tree.make_an_order.get_file_recording import GetFileRecording
            return GetFileRecording()
