import CTable, CDominoes, CPlayer, CRandom

domino_game = CDominoes.CDominoes()
domino_game.create_dominoes()
Player1 = CPlayer.CPlayer()
Player2 = CPlayer.CPlayer()
Random = CRandom.CRandom()
decks = Random.deal(domino_game)
Player1.set_deck(decks[0])
Player2.set_deck(decks[1])

TableRenderer = CTable.CTable()

firstPlayer = domino_game.determine_first(Player1, Player2)
print(f"first player is: {firstPlayer}")

PlayerOrder = []
if firstPlayer == 1:
    PlayerOrder.insert(0,Player1)
    PlayerOrder.insert(1,Player2)
else:
    PlayerOrder.insert(0,Player2)
    PlayerOrder.insert(1,Player1)

won = False
round = 1 # odd rounds will be the first player, evens will be the second
while won == False:
    #print(f"round {round}. board {len(domino_game.board)}. boneyard {len(domino_game.boneyard)}")
    result = PlayerOrder[round%2].play(domino_game)
    if result == "Won":
        print(f"{round%2} won!")
        exit()
    TableRenderer.display(domino_game)
    round += 1
