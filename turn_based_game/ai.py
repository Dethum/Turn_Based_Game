import random

class AIPlayer:
    def __init__(self, player):
        self.player = player

    def choose_move(self):
        return random.choice(self.player.moves)
