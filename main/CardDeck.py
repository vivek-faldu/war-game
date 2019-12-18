from main.Card import Card
from random import random


class CardDeck:

    def __init__(self):

        self.numCards = 0
        self.deck = [None]*52
        self.fill()

    def fill(self):
        index = 0
        for r in range(1,14):
            for s in range(1,5):
                self.deck[index] = Card(r,s)
                index+=1

        self.numCards = 52

    @staticmethod
    def myRandom(low, high):
        return int((high+1-low) * random()+ low)

    def getSize(self):
        return self.numCards

    def deal(self):
        if self.numCards == 0:
            return None

        self.numCards = self.numCards - 1
        return self.deck[self.numCards]

    def shuffle(self):
        for next in range(0,self.numCards-1):
            r = CardDeck.myRandom(next,self.numCards-1)
            temp = self.deck[next]
            self.deck[next] = self.deck[r]
            self.deck[r] = temp
