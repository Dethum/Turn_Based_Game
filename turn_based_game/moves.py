class Move:
    def __init__(self, name, power, move_type="attack"):
        self.name = name
        self.power = power
        self.type = move_type  # "attack" or "heal"

    def apply(self, user, target):
        if self.type == "attack":
            target.take_damage(self.power)
            print(f"{target.name} took {self.power} damage!")
        elif self.type == "heal":
            user.heal(self.power)
            print(f"{user.name} healed for {self.power} HP!")
