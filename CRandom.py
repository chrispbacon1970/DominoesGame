import random


# Class CRandom as sorting approach for the sequence that the
# domino pieces will be shown/picked;
class CRandom():
    def __init__(self):
        pass
    def deal(self, table):
        boneyard = table.boneyard
        player1_deck = []
        player2_deck = []
        for i in range(0,20):
            #print(len(boneyard))
            #drawn_domino = boneyard[random.randint(0, len(boneyard)-1)]
            drawn_domino = random.choice(boneyard)
            boneyard.remove(drawn_domino)
            if i%2 == 0:
                player1_deck.append(drawn_domino)
            else:
                player2_deck.append(drawn_domino)
        return (player1_deck, player2_deck)