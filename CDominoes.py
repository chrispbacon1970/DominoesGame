import random
class Domino:
    def __init__(self, front, back):
        #back is the left, right is the front
        self.front = front
        self.back = back

    def flip(self): # flips the domino
        a = self.front
        self.front = self.back
        self.back = a



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

    def withdraw_domino(self):
        if len(self.boneyard) != 0:
            selectedDomino = random.choice(self.boneyard)
            self.boneyard.remove(selectedDomino)
            return selectedDomino
        else:
            return "Empty"

    def play_domino(self, domino):
        #Play a domino and return if it was able to be played
        if len(self.board) == 0: # if the board is empty, the domino will be the first
            self.board.append(domino)
            return True

        #back is the left, right is the front
        '''if self.board[0].back == domino.front:
            self.board.insert(0, domino)
            return True # can place domino on board
        elif self.board[0].back == domino.back:
            domino.flip()
            self.board.insert(0, domino)
            return True  # can place domino on board
        elif self.board[len(self.board)-1].front == domino.back:
            self.board.append(domino)
            return True  # can place domino on board
        elif self.board[len(self.board)-1].front == domino.front:
            domino.flip()
            self.board.append(domino)
            return True  # can place domino on board
        else:
            return False # Cannot place domino'''


        if self.board[0].back == domino.front:
            self.board.insert(0, domino)
            return True  # can place domino on board
        elif self.board[len(self.board) - 1].front == domino.back:
            self.board.append(domino)
            return True  # can place domino on board
        else:
            domino.flip()
            if self.board[0].back == domino.front:
                self.board.insert(0, domino)
                return True  # can place domino on board
            elif self.board[len(self.board) - 1].front == domino.back:
                self.board.append(domino)
                return True  # can place domino on board
            else:
                domino.flip()
                #print(f"Failed because {self.board[0].back} != {domino.back} or {domino.front} ||||| {self.board[len(self.board) - 1].front} != {domino.back} or {domino.front}")
                return False
        #return None # idk how we got here

    def determine_first(self, Player1, Player2):
        BiggestDouble = None
        PlayerWithBiggestDouble = None

        # Find each player's biggest double if it exists
        for i in Player1.pieces:
            if i.front == i.back:
                if BiggestDouble == None:
                    BiggestDouble = i.front
                    PlayerWithBiggestDouble = 1
                else:
                    if i.front > BiggestDouble:
                        BiggestDouble = i.front
                        PlayerWithBiggestDouble = 1
        for i in Player2.pieces:
            if i.front == i.back:
                if BiggestDouble == None:
                    BiggestDouble = i.front
                    PlayerWithBiggestDouble = 2
                else:
                    if i.front > BiggestDouble:
                        BiggestDouble = i.front
                        PlayerWithBiggestDouble = 2

        #Neither has a double condition
        if BiggestDouble == None:
            numberDrawn = 1 # increment each withdraw from boneyard. odd will be 1's turn, even will be 2's
            while PlayerWithBiggestDouble == None: # keep drawing until a double is found
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
                    numberDrawn += 1 # increase the number of dominos drawn

        return PlayerWithBiggestDouble

    #def