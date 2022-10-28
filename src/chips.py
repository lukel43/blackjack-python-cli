class chips:
    def __init__(self):
        self.total = 500
        self.bet = 0

    def won_bet(self):
        self.total += self.bet
        print(f"You won {self.bet} chips.")
        print("Chips:", self.total)

    def won_blackjack(self):
        self.total += (1.5 * self.bet)
        print(f"You won {(self.bet * 1.5)} chips")
        print("Chips:", self.total)

    def lost_bet(self):
        self.total -= self.bet
        print(f"You lost {self.bet} chips!")
        print("Chips:", self.total)

    def take_bet(self):
        temp = int(input("How many chips would you like to bet?"))
        if self.total >= temp:
            self.bet = temp
        else:
            print("Your bet must be lower than your total!")
            self.bet = int(input("How many chips would you like to bet?"))

    def double_down(self):
        if (self.bet * 2) <= self.total:
            self.bet *= 2
        else:
            print("You dont have enough chips to double down!")
    def get_total(self):
        return self.total
