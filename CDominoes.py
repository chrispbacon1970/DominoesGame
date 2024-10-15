import random
class Domino:
    def __init__(self, front, back):
        self.front = front
        self.back = back
    def flip(self): # flips the domino
        a = self.front
        self.front = self.back
        self.back = a
    #def __repr__(self):
    #    print(f"[{self.front}|{self.back}]")


#Class CDominoes to contain the data structure with pieces;
class CDominoes:
    def __init__(self):
        self.boneyard = []
        self.board = []

    def create_dominoes(self): # create the dominoes set
        #create the domino set
        for x in range(0,7): # 7 is not inclusive in range()
            for y in range(x, 7):
                new_domino = Domino(x, y)
                self.boneyard.append(new_domino)

    def play_domino(self, domino):
        #Play a domino and return if it was able to be played
        if self.board[0].back == domino.front:
            self.board.insert(0, domino)
            return True # can place domino on board
        elif self.board[0].front == domino.back:
            domino = domino.flip()
            self.board.insert(0, domino)
            return True  # can place domino on board
        elif self.board[len(self.board)-1] == domino.front:
            self.board.append(domino)
            return True  # can place domino on board
        elif self.board[len(self.board)-1] == domino.back:
            domino = domino.flip()
            self.board.append(domino)
            return True  # can place domino on board
        else:
            return False # Cannot place domino

    def determine_first(self, Player1, Player2):
        BiggestDouble = None
        PlayerWithBiggestDouble = None

        # Find each player's biggest double if it exists
        for i in Player1.pieces:
            #print(i)
            if i.front == i.back:
                if BiggestDouble == None:
                    BiggestDouble = i.front
                    PlayerWithBiggestDouble = 1
                else:
                    if i.front > BiggestDouble:
                        BiggestDouble = i.front
                        PlayerWithBiggestDouble = 1
        for i in Player2.pieces:
            #print(i)
            if i.front == i.back:
                if BiggestDouble == None:
                    BiggestDouble = i.front
                    PlayerWithBiggestDouble = 2
                else:
                    if i.front > BiggestDouble:
                        BiggestDouble = i.front
                        PlayerWithBiggestDouble = 2

        #Neither had a double
        if BiggestDouble == None:
            numberDrawn = 1 # increment each withdraw from boneyard. odd will be 1's turn, even will be 2's
            while PlayerWithBiggestDouble == None:
                #drawnDomino = self.boneyard[0, len(self.boneyard)-1]
                drawnDomino = random.choice(self.boneyard)
                self.boneyard.remove(drawnDomino)
                if drawnDomino.front == drawnDomino.back:
                    if numberDrawn % 2 == 1: # determine who's turn it is that got a double
                        PlayerWithBiggestDouble = 1
                        break
                    else:
                        PlayerWithBiggestDouble = 2
                        break
                else:
                    numberDrawn += 1



        return PlayerWithBiggestDouble