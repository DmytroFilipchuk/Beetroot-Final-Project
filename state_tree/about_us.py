from state_tree.base_state import BaseState


class AboutUs(BaseState):
    msg = "About Us👇️"

    def __init__(self):
        super().__init__()
        self.buttons = [("Contacts ☎️", "contact"),
                        ("Spotify Playlist 🔊 ", "playlist_spotify"),
                        ("Website 🖥", "website"),
                        ("Main Menu 🎡", "menu")]

    def process(self, txt='', mark=bool) -> 'BaseState':
        from buttons_dict import buttons_dict
        if txt in buttons_dict.keys():
            return buttons_dict[txt]()



