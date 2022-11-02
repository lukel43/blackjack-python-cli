from card import card
import random

class deck:
    def __init__(self):
        self.cards = []
        self.create()

    def create(self):
        """Create a deck of 52 cards."""
        for s in ["Spades", "Clubs", "Hearts", "Diamonds"]:
            for v in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]:
                self.cards.append(card(s, v))

    def shuffle(self):
        """Shuffle all of the cards."""
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self):
        """Deal the cards."""
        if len(self.cards) > 1:
            return self.cards.pop(0)
