from state_tree.base_state import BaseState


class AboutUs(BaseState):
    msg = "About Usðï¸"

    def __init__(self):
        super().__init__()
        self.buttons = [("Contacts âï¸", "contact"),
                        ("Spotify Playlist ð ", "playlist_spotify"),
                        ("Website ð¥", "website"),
                        ("Main Menu ð¡", "menu")]

    def process(self, txt='', mark=bool) -> 'BaseState':
        from buttons_dict import buttons_dict
        if txt in buttons_dict.keys():
            return buttons_dict[txt]()



