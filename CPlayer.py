import random, CDominoes


#Class CPlayer to select a randomly picked and sequentially
#show the selected pieces.
class CPlayer():
    def __init__(self, name): # Initialization
        self.pieces = []
        self.skipped = False
        self.name = name

    def set_deck(self, deck): # Set the deck
        self.pieces = deck
    def play(self, table, lock): # plays any domino that works on the board
        self.skipped = False # Has the player skipped a turn?
        lock.acquire() # Acquire
        for i in self.pieces: # Check available pieces
            if table.play_domino(i) == True: # If it can be played
                self.pieces.remove(i) # 'Use up' the piece
                if len(self.pieces) == 0:
                    table.status = "Won"
                    lock.release()
                    return "Won"  # won the game
                lock.release()
                return "Played" # Was able to play the piece



        # If no working piece found in the deck, draw from boneyard until a working one is found
        dominoFound = False # has the piece been found?
        while dominoFound == False: # Loop until the domino is found
            new_domino = table.withdraw_domino() # Take a new domino
            if new_domino == "Empty": # If there is no new domino, skip the turn
                self.skipped = True
                lock.release()
                return
            if table.play_domino(new_domino) == True: # If a domino is found that works, play it
                lock.release()
                return "Played"
            else: # If the drawn domino does not work, add it to the deck
                self.pieces.append(new_domino)

        if len(self.pieces) == 0:
            table.status = "Won"
            lock.release()
            return "Won" # won the game