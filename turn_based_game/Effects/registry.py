from .poison import PoisonEffect
# from stun import StunEffect
# from regen import RegenEffect

EFFECT_REGISTRY = {
    "poison": lambda magnitude, duration: PoisonEffect(magnitude, duration),
    # "stun": lambda duration: StunEffect(duration),
    # "regen": lambda magnitude, duration: RegenEffect(magnitude, duration)
}
