class BaseState:
    msg = ''  # message that bot sends to the user

    def __init__(self):
        self.buttons = []  # list of tuples [(button_message, button_command), ]

    def process(self, txt='', mark=bool) -> 'BaseState':  # function that returns next UserStep (next class(BaseState))
        raise NotImplementedError
