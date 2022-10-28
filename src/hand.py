class hand:
    def __init__(self, dealer=False):
        self.dealer = dealer
        self.cards = []
        self.value = 0

    def add_to_hand(self, card):
        self.cards.append(card)


    def find_value(self):
        self.value = 0
        has_ace = False
        for card in self.cards:
            if card.val.isnumeric():
                self.value += int(card.val)
            else:
                if card.val == "A":
                    has_ace = True
                    self.value += 11
                else:
                    self.value += 10

        if has_ace and self.value > 21:
            self.value -= 10

    def get_value(self):
        self.find_value()
        return self.value

    def show_hand(self):
        if self.dealer:
            print("hidden")
            for i in range(1, len(self.cards)):
                print(self.cards[i])
            print()
        else:
            for card in self.cards:
                print(card)
            print("Value:", self.get_value())
