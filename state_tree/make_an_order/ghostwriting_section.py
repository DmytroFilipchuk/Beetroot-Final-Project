from state_tree.base_state import BaseState


class Ghostwriting(BaseState):
    msg = "Давай знайомитись! " \
          "Напиши назву колективу/виконавця ✏️"

    def __init__(self):
        super().__init__()
        self.buttons = [("Головне меню 🎡", "menu"), ("Назад ↩️", "back")]

    def process(self, txt='', mark=bool) -> 'BaseState':
        if txt == "menu":
            from state_tree.main_menu import MainMenu
            return MainMenu()
        if txt == "back":
            from state_tree.make_an_order.our_services import OurServices
            return OurServices()
        else:
            from state_tree.make_an_order.get_references import GetReferences
            return GetReferences()
