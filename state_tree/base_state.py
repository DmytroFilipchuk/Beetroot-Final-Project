class BaseState:

    msg = ''
    buttons = []

    def __init__(self):
        self.buttons = []

    def process(self, txt = '', authorized = bool) -> 'BaseState':

        raise NotImplementedError



