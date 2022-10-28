import random

class card:
    def __init__(self, suit, value):
        self.suit = suit
        self.val = value

    def __repr__(self):
        return " of ".join((self.val, self.suit))
