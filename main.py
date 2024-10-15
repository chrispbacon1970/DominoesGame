import CTable, CDominoes, CPlayer, CRandom

print("=== Initializing Game ===")

# Initialize the game and players
domino_game = CDominoes.CDominoes()
domino_game.create_dominoes()

Player1 = CPlayer.CPlayer()
Player2 = CPlayer.CPlayer()

Random = CRandom.CRandom()
decks = Random.deal(domino_game)

Player1.set_deck(decks[0])
Player2.set_deck(decks[1])

TableRenderer = CTable.CTable()

# Display initial hands
TableRenderer.displayhand(Player1, Player2)
TableRenderer.display_boneyard(domino_game)

firstPlayer = domino_game.determine_first(Player1, Player2)
if firstPlayer == Player2:
    offset = 1
else:
    offset = 0
print(f"first player is: Player{firstPlayer}")

# Determine the first player
PlayerOrder = []
if firstPlayer == 1:
    PlayerOrder.insert(0,Player1)
    PlayerOrder.insert(1,Player2)
else:
    PlayerOrder.insert(0,Player2)
    PlayerOrder.insert(1,Player1)

won = False
round = 1 # odd rounds will be the first player, evens will be the second
# Game loop
while won == False:
    print(f"round {round}. Player{(round+offset)%2+1}'s turn board {len(domino_game.board)}. boneyard {len(domino_game.boneyard)}")
    result = PlayerOrder[round%2].play(domino_game)
    if result == "Won":
        print(f"{round%2} won!")
        exit()
    TableRenderer.display(domino_game)
    TableRenderer.displayhand(Player1, Player2)
    round += 1
# Display the final result
TableRenderer.display_final_result(PlayerOrder)