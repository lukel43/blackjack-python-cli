from chips import chips
from card import card
from deck import deck
from hand import hand

import random



class blackjack():
    def __init__(self):
        pass

    def play(self):
        playing = True
        print("BLACKJACK")
        print("=========")
        print(f"Chips:", chips.get_total())

        while playing and chips.get_total() > 0:
            self.deck = deck()
            self.deck.shuffle()
            self.player_hand = hand()
            self.dealer_hand = hand(dealer = True)

            for i in range(2):
                card = self.deck.deal()
                self.player_hand.add_to_hand(card)
                card = self.deck.deal()
                self.dealer_hand.add_to_hand(card)



            chips.take_bet()
            print("Your Hand:")
            print("================")
            self.player_hand.show_hand()
            print("Chips:", chips.get_total())
            print("\nDealer Hand:")
            print("================")
            self.dealer_hand.show_hand()
            double = ""
            while double != "y" and double != "n":
                double = input("Would you like to double down(y/n)?").lower()
            if double == "y":
                chips.double_down()


            game_over = False
            while not game_over:
                player_blackjack, dealer_blackjack = self.check_blackjack()

                if player_blackjack or dealer_blackjack:
                    game_over = True
                    self.show_blackjack(player_blackjack, dealer_blackjack)
                    if player_blackjack:
                        chips.won_blackjack()
                    if dealer_blackjack:
                        chips.lost_bet()
                else:
                    hit = input("Hit or Stand(h/s)?").lower()
                    print()
                    if hit == "h":
                        hit = True
                    elif hit == "s":
                        hit = False
                    else:
                        hit = input("Hit or Stand(h/s)?").lower()
                        print()

                    if hit == True:
                        self.player_hand.add_to_hand(self.deck.deal())
                        self.player_hand.show_hand()

                        if self.player_over_21():
                            print("You went over, dealer wins.")
                            game_over = True
                            chips.lost_bet()

                    else:
                        player_val = self.player_hand.get_value()
                        dealer_val = self.dealer_hand.get_value()

                        while dealer_val < 17:
                            print("Dealer hits!")
                            print("New Dealer Hand")
                            print("====================")
                            self.dealer_hand.add_to_hand(self.deck.deal())
                            self.dealer_hand.show_hand()
                            dealer_val = self.dealer_hand.get_value()
                            if self.dealer_over_21():
                                print("The dealer went over, you win!")
                                game_over = True
                                chips.won_bet()

                        if not game_over:
                            print("Calculating...")
                            print("=====================")
                            print("Your Hand:", player_val)
                            print(f"Dealer Hand: {dealer_val} \n")

                            if player_val > dealer_val:
                                print("YOU WIN!!!")
                                chips.won_bet()
                            elif player_val == dealer_val:
                                print("You tied!")
                            else:
                                print("Dealer wins.")
                                chips.lost_bet()
                            game_over = True

            if chips.get_total() > 0:
                play_again = input("Would you like to play again?(Y/N):").upper()
                print()
                while play_again not in ["Y", "N"]:
                    play_again = input("Would you like to play again?(Y/N):").upper()
                if play_again == "Y":
                    game_over = False
                else:
                    print("Thanks for playing!")
                    print("Exiting...")
                    playing = False
            else:
                print("You ran out of chips!")
                print("Thanks for playing!")
                print("Exiting...")
                playing = False

    def check_blackjack(self):
        player = False
        dealer = False
        if self.player_hand.get_value() == 21:
            player = True
        if self.dealer_hand.get_value() == 21:
            dealer = True

        return player, dealer

    def show_blackjack(self, player_blackjack, dealer_blackjack):
        if player_blackjack and dealer_blackjack:
            print("You and the dealer have blackjack! Draw!")
        elif player_blackjack:
            print("You got blackjack! You win!")
        elif dealer_blackjack:
            print("Dealer has blackjack. Dealer wins.")
        print()

    def player_over_21(self):
        return self.player_hand.get_value() > 21

    def dealer_over_21(self):
        return self.dealer_hand.get_value() > 21
class card:
    def __init__(self, suit, value):
        self.suit = suit
        self.val = value

    def __repr__(self):
        return " of ".join((self.val, self.suit))

class deck:
    def __init__(self):
        self.cards = []
        self.create()

    def create(self):
        for s in ["Spades", "Clubs", "Hearts", "Diamonds"]:
            for v in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]:
                self.cards.append(card(s, v))

    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) > 1:
            return self.cards.pop(0)

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

chips = chips()
blackjack = blackjack()
blackjack.play()
