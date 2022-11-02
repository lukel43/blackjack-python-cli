class chips:
    def __init__(self, total):
        self.total = total
        self.bet = 0

    def set_total(self, new_total):
        """Set the total amount of chips for the player."""
        self.total = int(new_total)

    def won_bet(self):
        """Update total and output the amount won after a won hand."""
        self.total += self.bet
        print(f"You won {self.bet} chips.")

    def won_blackjack(self):
        """Update total and output the amount won after a won hand with blackjack."""
        self.total += (1.5 * self.bet)
        print(f"You won {(self.bet * 1.5)} chips")

    def lost_bet(self):
        """Update total and output the amount won after a lost hand."""
        self.total -= self.bet
        print(f"You lost {self.bet} chips!")

    def take_bet(self):
        """Prompt the player for a bet and test if the bet exceeds the player's total chips
           If it does not, confirm the bet."""
        temp = int(input("How many chips would you like to bet?"))
        if self.total >= temp:
            self.bet = temp
        else:
            print("Your bet must be lower than your total!")
            self.bet = int(input("How many chips would you like to bet?"))

    def double_down(self):
        """Test if the player has enough chips to double down, if able double the player's bet."""
        if (self.bet * 2) <= self.total:
            self.bet *= 2
        else:
            print("You dont have enough chips to double down!")
    def get_total(self):
        """Get the player's total number of chips."""
        return self.total
