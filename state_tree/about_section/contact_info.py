from state_tree.base_state import BaseState


class Contact_info(BaseState):
    msg = ""

    def process(self, txt='', authorized=bool) -> 'BaseState':
        from state_tree.about_us import AboutUs
        return AboutUs()

