
#Class CTable to show/display the sorted pieces;
class CTable:
    def __init__(self):
        pass

    def displayhand(self, Player1, Player2):
        print("Player 1's hand:", [f"[{p.front}|{p.back}]" for p in Player1.pieces])
        print("Player 2's hand:", [f"[{p.front}|{p.back}]" for p in Player2.pieces])

    def display_boneyard(self, table):
        print("Available pieces:", [f"[{p.front}|{p.back}]" for p in table.boneyard])

    def display(self, table):
        print("\n=== Current Table ===")
        for i in table.board:
            print(f"[{i.back}|{i.front}]", end=" ")
        print()

    def tie(self, Player1, Player2, table):
        print("\n===Final Result ===")
        print("The game resulted in a tie!")
        print("Player 1's hand:", [f"[{p.front}|{p.back}]" for p in Player1.pieces])
        print("Player 2's hand:", [f"[{p.front}|{p.back}]" for p in Player2.pieces])
        print("Final table:", [f"[{d.back}|{d.front}]" for d in table.board])


    def display_final_result(self, players, table):
        winner = players[0] if len(players[0].pieces) == 0 else players[1]
        loser = players[0] if winner == players[1] else players[1]

        print("\n=== Final Result ===")
        print(f"Player {players.index(winner) + 1} wins!")
        print(f"Player {players.index(loser) + 1}'s remaining pieces: ", [f"[{p.front}|{p.back}]" for p in loser.pieces])
        print("Final table:", [f"[{d.back}|{d.front}]" for d in table.board])