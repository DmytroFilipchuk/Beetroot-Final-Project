from state_tree.base_state import BaseState


class SessionMusician(BaseState):

    msg = "Provide basic information about the performance (date/venue) 📆 "

    def __init__(self):
        super().__init__()
        self.buttons = [("Main Menu 🎡", "menu"), ("Back ↩️", "back")]

    def process(self, txt='', mark = bool) -> 'BaseState':
        if txt == "menu":
            from state_tree.main_menu import MainMenu
            return MainMenu()
        if txt == "back":
            from state_tree.make_an_order.our_services import OurServices
            return OurServices()
        else:
            from state_tree.make_an_order.get_file_session import GetFileSession
            return GetFileSession()


