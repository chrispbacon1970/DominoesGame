import random


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