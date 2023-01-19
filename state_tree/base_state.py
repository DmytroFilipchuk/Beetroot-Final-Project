class BaseState:
    msg = ''  # message that bot sends to the user

    def __init__(self):
        self.buttons = []  # list of tuples [(button_message, button_command), ]

    def process(self, txt='', mark=bool) -> 'BaseState':
        raise NotImplementedError
