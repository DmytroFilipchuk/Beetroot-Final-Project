from state_tree.base_state import BaseState


class Confirmed(BaseState):

    msg = """The order has been successfully processed! 
    
To send it, type 'FFeel' and click send ✏️
P.S. After sending the order, expect a message 
(within 24 hours ⏱)"""

    def process(self, txt='', mark = bool) -> 'BaseState':
        from state_tree.main_menu import MainMenu
        return MainMenu()
