from state_tree.base_state import BaseState


class GetReferences(BaseState):

    msg = """Now let's move on to the references 🔗 

Send links to the reference tracks (3️⃣ link)
    
    
    """

    def __init__(self):
        super().__init__()
        self.buttons = [("Main Menu 🎡", "menu"),
                        ("Back ↩️", "back")]

    def process(self, txt='', mark = bool) -> 'BaseState':
        from buttons_dict import buttons_dict
        if txt in buttons_dict.keys():
            return buttons_dict[txt]()
        if txt == "back":
            from state_tree.make_an_order.ghostwriting_section import Ghostwriting
            return Ghostwriting()
        else:
            from state_tree.make_an_order.one_more_ref import One_more
            return One_more()





