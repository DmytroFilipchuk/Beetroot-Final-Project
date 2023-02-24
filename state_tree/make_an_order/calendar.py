from state_tree.base_state import BaseState


class Create_calendar(BaseState):
    msg = "Select a date 🗓"


    def process(self, txt='', mark=bool) -> 'BaseState':
        from buttons_dict import buttons_dict
        if txt in buttons_dict.keys():
            return buttons_dict[txt]()
        else:
            from state_tree.make_an_order.additional_info import AdditionalInfo
            return AdditionalInfo()




