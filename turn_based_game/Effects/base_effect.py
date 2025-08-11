from player import Player

class StatusEffect:
   
    """
    Represents a single status effect applied to a player or enemy.
    
    Attributes:
        name (str): Display name of the effect (e.g., 'Poison').
        effect_type (str): Logical category (e.g., 'dot', 'hot', 'stun', 'buff', 'shield').
        magnitude (int or float): Strength of the effect (e.g., damage per tick).
        duration (int): Turns remaining before the effect expires.
        timing (str): When the effect triggers ('start', 'end', 'on_action', 'on_receive').
        source (Player, optional): Who applied this effect.
        stackable (bool): Whether multiple instances can stack.
        max_stacks (int): Maximum allowed stacks if stackable.
        priority (int): Determines processing order when multiple effects share the same timing.
        meta (dict): Optional custom data for unique behavior.
    """

    def __init__(self, name, effect_type, magnitude, duration, timing,
                 source=None, stackable=False, max_stacks=1, priority=0, meta=None):
        self.name = name
        self.effect_type = effect_type
        self.magnitude = magnitude
        self.duration = duration
        self.timing = timing
        self.source = source
        self.stackable = stackable
        self.max_stacks = max_stacks
        self.priority = priority
        self.meta = meta or {}

    # --------------------
    # Lifecycle Methods
    # --------------------
    def on_apply(self, target):
        """
        Called once when the effect is first applied.
        Example: Display message, modify stats, initialize counters.
        """
        pass

    def on_start_turn(self, target):
        """
        Called at the start of the target's turn if timing == 'start'.
        Example: Apply DOT damage, check stun and set skip flag.
        """
        pass

    def on_before_action(self, user, target, move):
        """
        Called before the target executes a move if timing == 'on_action'.
        Example: Reduce outgoing damage, block move.
        """
        pass

    def on_after_action(self, user, target, move):
        """
        Called after the move resolves.
        Example: Trigger damage reflection, apply follow-up effects.
        """
        pass

    def on_end_turn(self, target):
        """
        Called at the end of the target's turn if timing == 'end'.
        Example: Heal over time, decay buff strength.
        """
        pass

    def on_receive_damage(self, target, amount, source):
        """
        Called when the target takes damage if timing == 'on_receive'.
        Example: Shield reduces damage, counterattack applies.
        """
        pass

    def on_expire(self, target):
        """
        Called once when the effect's duration reaches 0.
        Example: Remove stat buffs, display expiration message.
        """
        pass

    # --------------------
    # Utility Methods
    # --------------------
    def tick(self):
        """
        Decrease the effect's duration by 1 turn.
        Should be called after each turn phase where duration decreases.
        """
        pass

    def is_expired(self):
        """
        Returns True if the effect has no remaining duration.
        """
        pass

    def can_stack_with(self, other_effect) -> bool:
        """
        Determines if this effect can stack with another effect.
        Override in subclasses for custom logic.
        """
        return False