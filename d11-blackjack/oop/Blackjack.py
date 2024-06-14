
import random as rand

class AllCards():
    def __init__(self):
        self.cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

class Blackjack():
    def __init__(self, card_class):
        self.deck = card_class.cards
        self.curr = []

    def draw(self):
        rand_idx = rand.randint(0, len(self.deck) - 1)
        self.curr.append(self.deck[rand_idx])
        self.deck.pop(rand_idx)

    def check11(self):  # Check if there is 11 and meet condition
        if 11 in self.curr:
            find_11 = self.curr.index(11)
            if sum(self.curr) < 21:
                self.curr[find_11] = 1

            elif sum(self.curr) > 21:
                self.curr[find_11] = 1

    def check21(self):
        if sum(self.curr) == 21:
            return True
          
