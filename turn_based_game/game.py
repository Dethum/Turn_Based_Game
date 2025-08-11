import asyncio
from moves import load_moves_from_json
from player import Player

def process_start_of_turn_effects(player):
    for effect in list(player.active_effects):
        if effect.timing == "start":
            effect.on_start_turn(player)
            if effect.is_expired():
                player.active_effects.remove(effect)

def process_end_of_turn_effects(player):
    for effect in list(player.active_effects):
        if effect.timing == "end":
            effect.on_end_turn(player)
            if effect.is_expired():
                player.active_effects.remove(effect)

async def player_turn(player, enemy):
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
    process_start_of_turn_effects(ai)
    move = ai.moves[0]
    move.apply(ai, player)
    await asyncio.sleep(0.5)
    process_end_of_turn_effects(ai)

async def main():
    moves = load_moves_from_json("data/moves.json")
    player1 = Player("Hero", 50, moves)
    player2 = Player("Enemy", 50, moves)  # AI with same move for test

    for _ in range(5):
        print("\n--- Player Turn ---")
        await player_turn(player1, player2)
        if player2.hp <= 0:
            print(f"{player2.name} has been defeated!")
            break

        print("\n--- Enemy Turn ---")
        await ai_turn(player2, player1)
        if player1.hp <= 0:
            print(f"{player1.name} has been defeated!")
            break

if __name__ == "__main__":
    asyncio.run(main())
