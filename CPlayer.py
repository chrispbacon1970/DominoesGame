import random, CDominoes


#Class CPlayer to select a randomly picked and sequentially
#show the selected pieces.
class CPlayer():
    def __init__(self):
        self.pieces = []

    def set_deck(self, deck):
        self.pieces = deck
    def play(self):
        selected_domino = self.pieces[random.randint(0, len(self.pieces))]
        self.pieces.remove(selected_domino)
        return selected_domino
    def determine_first(self, other, table):
        Player1BiggestDouble = None
        Player2BiggestDouble = None

        for i in range(1, 7):
            print(i)

            if CDominoes.Domino(i,i) in self.pieces:
                Player1BiggestDouble = i
        for i in range(1, 7):
            print(i)

            if CDominoes.Domino(i,i) in other.pieces:
                Player2BiggestDouble = i
        if Player1BiggestDouble == Player2BiggestDouble:
            Player1Turn=True

            drawn_domino = table.boneyard[random.randint(0, len(table.boneyard))]
            table.boneyard.remove(drawn_domino)
