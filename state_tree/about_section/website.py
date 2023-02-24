from state_tree.base_state import BaseState


class Website(BaseState):
    msg = ""

    def process(self, txt='', mark=bool) -> 'BaseState':
        from buttons_dict import buttons_dict
        if txt in buttons_dict.keys():
            return buttons_dict[txt]()
        else:
            from state_tree.about_us import AboutUs
            return AboutUs()