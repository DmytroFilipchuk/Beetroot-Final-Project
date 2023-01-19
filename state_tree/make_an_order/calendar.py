from state_tree.base_state import BaseState


class Create_calendar(BaseState):
    msg = "Обери дату 🗓"


    def process(self, txt='', mark=bool) -> 'BaseState':
            from state_tree.make_an_order.additional_info import AdditionalInfo
            return AdditionalInfo()

