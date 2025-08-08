import asyncio
from player import Player
from moves import Move
from ai import AIPlayer

async def player_turn(player, opponent):
    print(f"\n--- {player.name}'s Turn ---")
    move = player.choose_move()
    move.apply(player, opponent)
    await asyncio.sleep(1)

async def ai_turn(ai, player):
    print(f"\n--- {ai.player.name}'s Turn ---")
    move = ai.choose_move()
    move.apply(ai.player, player)
    await asyncio.sleep(1)

async def main():
    # Example setup
    tackle = Move("Tackle", 10)
    heal = Move("Heal", 5, "heal")

    player = Player("Hero", 50, [tackle, heal])
    enemy = Player("Goblin", 40, [tackle])
    ai = AIPlayer(enemy)

    while player.is_alive() and enemy.is_alive():
        await player_turn(player, enemy)
        if not enemy.is_alive():
            print(f"{enemy.name} has been defeated!")
            break

        await ai_turn(ai, player)
        if not player.is_alive():
            print(f"{player.name} has been defeated!")
            break

if __name__ == "__main__":
    asyncio.run(main())
