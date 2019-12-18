class Pile:

    def __init__(self):
        self.pile = [None] * 52
        self.front = 0
        self.end = 0

    def getSize(self):
        return self.end - self.front

    def clear(self):
        self.front = 0
        self.end = 0

    def addCard(self,card):
        self.pile[self.end] = card
        self.end +=1

    def addCards(self, p):

        while(p.getSize()>0):
            self.addCard(p.nextCard())

    def nextCard(self):

        if self.front == self.end:
            return None

        c = self.pile[self.front]
        self.front += 1
        return c

