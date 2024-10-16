import random


# Class CRandom as sorting approach for the sequence that the
# domino pieces will be shown/picked;
class CRandom():
    def __init__(self): # initialization
        pass
    def deal(self, table): # deal the dominoes to the players
        boneyard = table.boneyard # get the boneyard
        player1_deck = [] # initialize the decks
        player2_deck = []
        for i in range(0,20): # draw 20 dominos and give half to each deck
            drawn_domino = random.choice(boneyard)
            boneyard.remove(drawn_domino)
            if i%2 == 0:
                player1_deck.append(drawn_domino)
            else:
                player2_deck.append(drawn_domino)
        return (player1_deck, player2_deck) # return both decks