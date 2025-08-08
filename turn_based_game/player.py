class Player:
    def __init__(self, name, hp, moves):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.moves = moves

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, amount):
        self.hp = max(self.hp - amount, 0)

    def heal(self, amount):
        self.hp = min(self.hp + amount, self.max_hp)

    def choose_move(self):
        # Placeholder for player input — override in AI
        print(f"\n{self.name}'s moves:")
        for i, move in enumerate(self.moves, start=1):
            print(f"{i}. {move.name} ({move.power})")
        choice = int(input("Choose a move: ")) - 1
        return self.moves[choice]
