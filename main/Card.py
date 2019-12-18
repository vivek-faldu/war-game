class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit


    def toString(self):
        val = None
        suitList = ["","Clubs", "Diamonds", "Hearts", "Spades"]
        if self.rank == 1:
            val = "Ace"

        elif self.rank == 11:
            val = "Jack"

        elif self.rank == 12:
            val = "Queen"

        elif self.rank == 13:
            val = "King"

        else:
            val = str(self.rank)

        return val + " of " + suitList[self.suit]

    def __eq__(self, other):
        return self.getRank() == other.getRank() and self.getSuit() == other.getSuit()

    def __lt__(self, other):
            if self.getRank() == 1:
                self_rank = 14
            else:
                self_rank = self.getRank()

            if other.getRank() == 1:
                other_rank = 14
            else:
                other_rank = other.getRank()

            return self_rank < other_rank

