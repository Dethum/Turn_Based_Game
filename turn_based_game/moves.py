import random
import json
from Effects.registry import EFFECT_REGISTRY

class Move:
    def __init__(self, name, type, power, crit_chance=0.15, miss_chance=0.1, status_effect=None):
        self.name = name
        self.type = type
        self.power = power
        self.crit_chance = crit_chance
        self.miss_chance = miss_chance
        self.status_effect = status_effect  # dict with name, magnitude, duration

    def apply(self, user, target):
        """
        Apply the move's damage and any status effect.
        """

     # Roll for miss
        if random.random() < self.miss_chance:
            print(f"{user.name}'s {self.name} missed!")
            return

        # Roll for crit
        damage = self.power
        if random.random() < self.crit_chance:
            damage *= 2
            print("Critical hit!")

        if self.type == "healing":
            user.hp += self.power
            user.hp = min(user.hp, user.max_hp) # cap at max HP
            print(f"{user.name} heals for {self.power} HP!")

        # Apply base damage
        elif self.power > 0:
            target.hp -= self.power
            print(f"{user.name} hits {target.name} for {self.power} damage!")

        # Apply status effect if any
        if self.status_effect:
            effect_name = self.status_effect["name"]
            magnitude = self.status_effect["magnitude"]
            duration = self.status_effect["duration"]

            if effect_name in EFFECT_REGISTRY:
                # Create effect instance
                new_effect = EFFECT_REGISTRY[effect_name](magnitude, duration)

                # Check if target already has this effect
                for e in target.active_effects:
                    if e.can_stack_with(new_effect):
                        e.stack_with(new_effect)
                        break
                else:
                    target.active_effects.append(new_effect)
                    new_effect.on_apply(target)

def load_moves_from_json(path):
    with open(path, "r") as f:
        moves_data = json.load(f)
    return [
        Move(
            m["name"],
            m["type"],
            m["power"],
            m.get("crit_chance", 0.15),
            m.get("miss_chance", 0.1),
            m.get("status_effect")
        )
        for m in moves_data
    ]
