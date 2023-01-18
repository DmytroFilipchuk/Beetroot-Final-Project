from state_tree.base_state import BaseState


class SessionMusician(BaseState):

    msg = "Вкажи основні данні про виступ (дата/місце) 📆 "

    def __init__(self):
        super().__init__()
        self.buttons = [("Головне меню 🎡", "menu"), ("Назад ↩️", "back")]

    def process(self, txt='', authorized = bool) -> 'BaseState':
        if txt == "menu":
            from state_tree.main_menu import Main_menu
            return Main_menu()
        if txt == "back":
            from state_tree.make_an_order.our_services import OurServices
            return OurServices()
        else:
            from state_tree.make_an_order.get_file_session import GetFileSession
            return GetFileSession()


