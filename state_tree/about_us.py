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

        if txt == "contact":
            from state_tree.about_section.contact_info import Contact_info
            return Contact_info()

        if txt == "playlist_spotify":
            from state_tree.about_section.our_playlist import MyPlaylist
            return MyPlaylist()

        if txt == "website":
            from state_tree.about_section.website import Website
            return Website()

        if txt == "menu":
            from state_tree.main_menu import MainMenu
            return MainMenu()
