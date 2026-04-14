from utils import draw_hp_bar

class Player:
    def __init__(self, name, hp, moves):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.moves = moves
        self.active_effects = []  # store status effects here

    def display_hp(self):
        draw_hp_bar(self.name, self.hp, self.max_hp)
