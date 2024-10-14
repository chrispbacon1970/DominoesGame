class dominoe():
    def __init__(self, front, back):
        self.front = front
        self.back = back
    def __repr__(self):
        print(f"[{self.front}|{self.back}]")


#Class CDominoes to contain the data structure with pieces;
class CDominoes():
    def __init__(self):
        self.boneyard = []
        self.board = []

    def create_dominoes(self): #
        for x in range(1,6):
            for y in range(x, 6):
                new_dominoe = dominoe(x, y)
                self.boneyard.append(new_dominoe)

