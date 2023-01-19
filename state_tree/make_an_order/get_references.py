from state_tree.base_state import BaseState


class GetReferences(BaseState):

    msg = """Тепер перейдемо до референсів 🔗 

Надішли посилання на треки-референси (3️⃣ посилання) 
    
    
    """

    def __init__(self):
        super().__init__()
        self.buttons = [("Головне меню 🎡", "menu"),
                        ("Назад ↩️", "back")]

    def process(self, txt='', mark = bool) -> 'BaseState':
        if txt == "menu":
            from state_tree.main_menu import MainMenu
            return MainMenu()
        if txt == "back":
            from state_tree.make_an_order.ghostwriting_section import Ghostwriting
            return Ghostwriting()
        else:
            from state_tree.make_an_order.one_more_ref import One_more
            return One_more()





