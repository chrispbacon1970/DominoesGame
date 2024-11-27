# Authors: Bennett, Zachary, and Nathan

import CTable, CDominoes, CPlayer, CRandom
import threading

print("=== Initializing Game ===")

# Initialize the game and players
domino_game = CDominoes.CDominoes()
domino_game.create_dominoes()

Player1 = CPlayer.CPlayer("Player1")
Player2 = CPlayer.CPlayer("Player2")

Random = CRandom.CRandom()
decks = Random.deal(domino_game)

Player1.set_deck(decks[0])
Player2.set_deck(decks[1])

TableRenderer = CTable.CTable()

# Display initial hands
TableRenderer.displayhand(Player1, Player2)
TableRenderer.display_boneyard(domino_game)

# Determind first player
firstPlayer = domino_game.determine_first(Player1, Player2)
if firstPlayer == Player2:
    offset = 1
else:
    offset = 0
print(f"first player is: Player{firstPlayer}")

# Setup the player threads
#Player1Thread = threading.Thread(target=Player1.play,name="player1", args=(domino_game,))
#Player2Thread = threading.Thread(target=Player2.play,name="player2", args=(domino_game,))


# Setup the array for players
PlayerOrder = []
if firstPlayer == 1:
    PlayerOrder.insert(0,Player1)
    PlayerOrder.insert(1,Player2)
else:
    PlayerOrder.insert(0,Player2)
    PlayerOrder.insert(1,Player1)

won = False
round = 0 # odd rounds will be the first player, evens will be the second

mutex_lock = threading.Lock() # create the Mutex

# Game loop
while won == False:
    round += 1
    print(f"This round is player {(round+offset-1)%2+1}'s turn") # Announce who's turn it is
    if ((round+offset)%2) == 1:
        player = Player1
        Player1Thread = threading.Thread(target=Player1.play, name="player1", args=(domino_game, mutex_lock))
        result = Player1Thread.start()
        Player1Thread.join() # Wait for thread to finish before continuing execution. The
    else:
        player = Player2
        Player2Thread = threading.Thread(target=Player2.play, name="player2", args=(domino_game, mutex_lock))
        Player2Thread.start()
        Player2Thread.join()

    #print(domino_game.status) # Debug to determine if the current round has a winner.
    if domino_game.status == "Won":
        break # exit the loop to the final display
    if Player1.skipped == True and Player2.skipped == True: # if tied, special tie condition
        TableRenderer.tie(Player1, Player2, domino_game) # Show the tie
        exit()
    TableRenderer.display(domino_game, round) # Display the board
    TableRenderer.displayhand(Player1, Player2) # Display the hands

    

# Display the final result
TableRenderer.display_final_result(PlayerOrder, domino_game)