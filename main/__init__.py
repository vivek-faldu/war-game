from main.Game import Game


if __name__ == "__main__":

    g = Game()
    g.play()

    winner = g.getWinner()

    if winner == None:
        print("Tie")

    else:
        print("Winner is " + winner.getName())