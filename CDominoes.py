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
        if self.board[0].back == domino.front: #
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