from main.CardDeck import CardDeck
from main.Player import Player
from main.Pile import Pile

class Game:

    def play(self):

        cardDeck = CardDeck()
        cardDeck.shuffle()
        self.p1 = Player("Player1")
        self.p2 = Player("Player2")

        while(cardDeck.getSize() >= 1):
            self.p1.collectCard(cardDeck.deal())
            self.p2.collectCard(cardDeck.deal())

        self.p1.useWonPile()
        self.p2.useWonPile()

        down = Pile()

        for t in range(1,1001):

            if not self.enoughCards(1):
                break

            c1 = self.p1.playCard()
            c2 = self.p2.playCard()

            print("Turn "+ str(t)+ " :")
            print(self.p1.getName() + " : " + c1.toString() +"")
            print(self.p2.getName() + " : " + c2.toString() + "")

            if c1 > c2:
                self.p1.collectCard(c1)
                self.p1.collectCard(c2)

            elif c2 > c1:
                self.p2.collectCard(c1)
                self.p2.collectCard(c2)

            else:
                down.clear()
                down.addCard(c1)
                down.addCard(c2)
                done = False

                while(not done):
                    num = c1.getRank()
                    if (not self.enoughCards(num)):
                        break

                    print("War!! Players put down "+ str(num) + " cards")

                    for m in range(1,num+1):
                        c1 = self.p1.playCard()
                        c2 = self.p2.playCard()
                        down.addCard(c1)
                        down.addCard(c2)

                    print(self.p1.getName() + " : " + c1.toString() + "")
                    print(self.p2.getName() + " : " + c2.toString() + "")
                    if c1 > c2:
                        self.p1.collectCards(down)
                        done = True

                    elif c2 > c1:
                        self.p2.collectCards(down)
                        done = True


    def getWinner(self):

        if (self.p1.numCards() > self.p2.numCards() and self.p2.numCards()==0):
            return self.p1

        elif (self.p2.numCards() > self.p1.numCards() and self.p1.numCards()==0):
            return self.p2

        else:
            return None


    def enoughCards(self,n):
        if self.p1.numCards() < n or self.p2.numCards() < n:
            return False
        return True