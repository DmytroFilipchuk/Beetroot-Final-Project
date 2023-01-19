from state_tree.base_state import BaseState


class Confirmed(BaseState):

    msg = """Замовлення успішно оброблено! Для відправки напиши ✏️ 'FFeel' 
          
P.S. Після відправки замовлення очікуй на повідомлення 
(в межах 24 годин ⏱)"""

    def process(self, txt='', mark = bool) -> 'BaseState':
        from state_tree.main_menu import MainMenu
        return MainMenu()
