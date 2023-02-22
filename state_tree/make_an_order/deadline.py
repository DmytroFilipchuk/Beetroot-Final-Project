from state_tree.base_state import BaseState


class Deadline(BaseState):

    msg = "Select the desired deadline 🕒  "

    def __init__(self):
        super().__init__()
        self.buttons = [("Open the calendar 📅", "calendar") , ("Main Menu 🎡", "menu")]

    def process(self, txt='', mark = bool) -> 'BaseState':

        if txt == "menu":
            from state_tree.main_menu import MainMenu
            return MainMenu()

        if txt == "calendar":
            from state_tree.make_an_order.calendar import Create_calendar
            return Create_calendar()

        else:
            from state_tree.make_an_order.additional_info import AdditionalInfo
            return AdditionalInfo()

