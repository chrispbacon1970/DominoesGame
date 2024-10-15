

#Class CTable to show/display the sorted pieces;
class CTable():
    def __init__(self):
        pass

    def display(self, table): # render the board
        board = table.board
        for i in board:
            print(f"[{i.back}|{i.front}]", end=" ")
        print()