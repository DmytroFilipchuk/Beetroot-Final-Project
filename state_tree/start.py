from state_tree.base_state import BaseState

class Authorization(BaseState):

    msg = 'Enter your phone number in the following format -  +380... for authorization 📝'

    def process(self, txt = '', mark = bool) -> 'BaseState':
        from buttons_dict import buttons_dict
        if txt in buttons_dict.keys():
            return buttons_dict[txt]()
        else:
            from state_tree.main_menu import MainMenu
            return MainMenu()







class Start(BaseState):

    msg = """Hello! 😁 I am your assistant from <a href=
    'http://ffeelmusic.tilda.ws/'>FFeel Music Records</a>

You can use me to place orders or use special FFeelTools 🎹 

But I am still very young, so if you have any difficulties, 
just send a text message to - @philipchuk_d 📲

<a href=
    'https://open.spotify.com/playlist/6Ud9RGICEhn84flFAfFeTM?si=c4a6827a19e34a3f'>Our Spotify playlist 😎</a>

Let's get started!"""


    def process(self, txt = '', mark = bool) -> 'BaseState':
        if mark is True:
            from state_tree.main_menu import MainMenu
            return MainMenu()
        from buttons_dict import buttons_dict
        if txt in buttons_dict.keys():
            return buttons_dict[txt]()
        else:
            return Authorization()
