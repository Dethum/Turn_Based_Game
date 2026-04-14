import asyncio
from pathlib import Path
from moves import load_moves_from_json
from player import Player

def process_start_of_turn_effects(player):
    """"
    Processes effects that trigger at the start of the turn.
    """
    for effect in list(player.active_effects):
        if effect.timing == "start":
            effect.on_start_turn(player)
            if effect.is_expired():
                player.active_effects.remove(effect)

def process_end_of_turn_effects(player):
    """"
    Processes effects that trigger at the end of the turn.
    """
    for effect in list(player.active_effects):
        if effect.timing == "end":
            effect.on_end_turn(player)
            if effect.is_expired():
                player.active_effects.remove(effect)

async def player_turn(player, enemy):
    """
    Handles the player's turn, including move selection and applying effects.
    """
    process_start_of_turn_effects(player)
    player.display_hp()

    enemy.display_hp()

    #show moves
    print("\nChoose your move:")
    for i, move in enumerate(player.moves):
        print(f"{i + 1}. {move.name} (Type: {move.type}, Power: {move.power})")

    while True:
        try:
            choice = int(input("Enter the number of your move: ")) - 1
            if 0 <= choice < len(player.moves):
                chosen_move = player.moves[choice]
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    # Use move chosen
    chosen_move.apply(player, enemy)
    await asyncio.sleep(0.5)
    process_end_of_turn_effects(player)

async def ai_turn(ai, player):
    """"
    Handles the AI's turn, including move selection and applying effects.
    """
    process_start_of_turn_effects(ai)
    move = ai.moves[0]
    move.apply(ai, player)
    await asyncio.sleep(0.5)
    process_end_of_turn_effects(ai)
    
def check_for_death(player): #checks to see if either player has been defeated
    if player.hp <= 0:
        print(f"{player.name} has been defeated!")
        return True
    return False

async def main():
    moves_path = Path(__file__).resolve().parent / "data" / "moves.json"
    moves = load_moves_from_json(moves_path)
    player1 = Player("Hero", 50, moves)
    player2 = Player("Enemy", 50, moves)

    for _ in range(5):
        print("\n--- Player Turn ---")
        if check_for_death(player2):
            break
        if check_for_death(player1):
            break
        await player_turn(player1, player2)
       

        print("\n--- Enemy Turn ---")
        if check_for_death(player1):
            break
        if check_for_death(player2):
            break
        await ai_turn(player2, player1)

    
       

if __name__ == "__main__":
    asyncio.run(main())
