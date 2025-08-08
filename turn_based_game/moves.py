import asyncio
import random  
from utils import roll_chance


class Move:
    def __init__(self, name, power, move_type="attack", crit_chance=0.1, miss_chance=0.05):
        self.name = name
        self.power = power
        self.type = move_type 
        self.crit_chance = crit_chance
        self.miss_chance = miss_chance

    async def apply(self, user, target):
        await asyncio.sleep(0.5)  # Simulate delay for move application

        # miss chance
        if roll_chance(self.miss_chance):
            print(f"{user.name}'s {self.name} missed!")
            return

        # base effect
        amount = self.power

        #critical hit chance (only for attacks)
        if self.type == "attack" and random.random() < self.crit_chance:
            amount *= 2
            print(f" ⚡ Critical hit! {user.name} dealt double damage! ⚡")

        if self.type == "attack":
            target.take_damage(amount)
            print(f"{target.name} took {amount} damage!")
        elif self.type == "heal":
            user.heal(amount)
            print(f"{user.name} healed for {amount} HP!")

    async def _heal_animation(self, user):
        # Simulate a healing animation
        await asyncio.sleep(0.5)
        print(f"{user.name} is surrounded by a warm light!")
