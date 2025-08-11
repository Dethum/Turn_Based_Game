from .base_effect import StatusEffect

class PoisonEffect(StatusEffect):
    """
    A damage-over-time (DoT) effect that applies damage at the start of each turn.
    """

    def __init__(self, magnitude, duration, source=None):
        super().__init__(
            name="Poison",
            effect_type="dot",
            magnitude=magnitude,
            duration=duration,
            timing="start",       # triggers at the start of the target's turn
            source=source,
            stackable=True,       # poison can stack
            max_stacks=3,         # cap number of stacks
            priority=0
        )
        self.stacks = 1  # track how many times this effect is stacked

    def on_apply(self, target):
        """
        Called when poison is first applied.
        """
        print(f"{target.name} has been poisoned! ({self.magnitude} damage for {self.duration} turns)")

    def on_start_turn(self, target):
        """
        Applies poison damage at the start of each turn.
        """
        # Apply damage
        total_damage = self.magnitude * self.stacks
        target.hp -= total_damage

        # Display message
        print(f"{target.name} takes {total_damage} poison damage! ({self.duration} turns remaining)")

        # Tick down duration
        self.tick()

        # Check expiration
        if self.is_expired():
            self.on_expire(target)

    def on_expire(self, target):
        """
        Called when poison runs out.
        """
        print(f"{target.name} is no longer poisoned.")

    def can_stack_with(self, other_effect):
        """
        Stacking logic: increases stacks if under max_stacks.
        """
        return (
            isinstance(other_effect, PoisonEffect) and
            self.stacks < self.max_stacks
        )

    def stack_with(self, other_effect):
        """
        Increase stack count and possibly refresh duration.
        """
        self.stacks = min(self.stacks + 1, self.max_stacks)
        self.duration = max(self.duration, other_effect.duration)
        print(f"Poison on {other_effect.source.name if other_effect.source else 'target'} has stacked! ({self.stacks} stacks)")
