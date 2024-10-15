import CTable, CDominoes, CPlayer, CRandom

domino_game = CDominoes.CDominoes()
domino_game.create_dominoes()
Player1 = CPlayer.CPlayer()
Player2 = CPlayer.CPlayer()
Random = CRandom.CRandom()
decks = Random.deal(domino_game)
Player1.set_deck(decks[0])
Player2.set_deck(decks[1])

firstPlayer = domino_game.determine_first(Player1, Player2)
print(f"first player {firstPlayer}")
