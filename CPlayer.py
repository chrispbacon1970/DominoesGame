import random, CDominoes


#Class CPlayer to select a randomly picked and sequentially
#show the selected pieces.
class CPlayer():
    def __init__(self):
        self.pieces = []
        self.skipped = False

    def set_deck(self, deck):
        self.pieces = deck
    def play(self, table): # plays any domino that works on the board
        self.skipped = False
        if len(self.pieces) == 0:
            return "Won"
        for i in self.pieces:
            if table.play_domino(i) == True:
                self.pieces.remove(i)
                return "Played"
        dominoFound = False
        while dominoFound == False:
            new_domino = table.withdraw_domino()
            if new_domino == "Empty":
                self.skipped = True
                return
            if table.play_domino(new_domino) == True:
                return "Played"
            else:
                self.pieces.append(new_domino)
