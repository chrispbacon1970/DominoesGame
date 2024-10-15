import random, CDominoes


#Class CPlayer to select a randomly picked and sequentially
#show the selected pieces.
class CPlayer():
    def __init__(self):
        self.pieces = []

    def set_deck(self, deck):
        self.pieces = deck
    def play(self, table): # plays any domino that works on the board
        if len(self.pieces) == 0:
            return "Won"
        for i in self.pieces:
            if table.play_domino == True:
                self.pieces.remove(i)
                return "Played"
        dominoFound = False
        while dominoFound == False:
            new_domino = table.withdraw_domino()
            if new_domino == "Empty":
                print("The boneyard is empty when attempting to withdraw another domino. Terminating...")
                exit()
            if table.play_domino(new_domino) == True:
                return "Played"
            else:
                self.pieces.append(new_domino)
