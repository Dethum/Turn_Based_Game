from colorama import Fore
import asyncio
from player import Player
from moves import Move
from ai import AIPlayer
from utils import slow_print, print_separator 

async def player_turn(player, opponent):
    print(f"\n--- {player.name}'s Turn ---")
    player.display_hp()
    opponent.display_hp()
    move = player.choose_move()
    await move.apply(player, opponent)

async def ai_turn(ai, player):
    print(f"\n--- {ai.player.name}'s Turn ---")
    ai.player.display_hp()
    player.display_hp()
    move = ai.choose_move()
    print(f"{ai.player.name} chose {move.name}!")
    await move.apply(ai.player, player)

async def main():
   # Define moves
    tackle = Move("Tackle", 10)
    heal = Move("Heal", 7, "heal")
    power_strike = Move("Power Strike", 15, crit_chance=0.1, miss_chance=0.15)

    player = Player("Hero", 50, [tackle, heal, power_strike])
    enemy = Player("Goblin", 40, [tackle, power_strike])
    ai = AIPlayer(enemy)

    slow_print("⚔️ Welcome to Battle Arena! ⚔️", 0.05, color=Fore.CYAN)
    print_separator("=")
    await asyncio.sleep(1)

   # Gameplay loop
    while player.is_alive() and enemy.is_alive():
        await player_turn(player, enemy)
        if not enemy.is_alive():
            print(f"{enemy.name} has been defeated. You win! 🎉")
            break

        await ai_turn(ai, player)
        if not player.is_alive():
            print(f"💀 {player.name} has been defeated. Game over.")
            break

if __name__ == "__main__":
    asyncio.run(main())
