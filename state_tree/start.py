from state_tree.base_state import BaseState

class Authorization(BaseState):

    msg = ' Напиши свій номер телефону у форматі +380... для авторизації 📝}'

    def process(self, txt = '', mark = bool) -> 'BaseState':
        from state_tree.main_menu import MainMenu
        return MainMenu()





class Start(BaseState):

    msg = """Привіт! 😁 Я - твій помічник від <a href=
    'http://project6565316.tilda.ws/'>FFeel Music Records</a>

До мене ти можеш звертатись з приводу замовлень 
або ж скористатись спецільними FFeelTools 🎹 

Але я ще дуже молодий, тому якщо у тебе виникнуть складнощі
в роботі, напиши сюди - @philipchuk_d 📲

<a href=
    'https://open.spotify.com/playlist/6Ud9RGICEhn84flFAfFeTM?si=c4a6827a19e34a3f'>Наш Spotify плейлист 😎</a>

Давай розпочнемо!"""


    def process(self, txt = '', mark = bool) -> 'BaseState':
        if mark is True:
            from state_tree.main_menu import MainMenu
            return MainMenu()
        else:
            return Authorization()
