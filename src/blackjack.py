from chips import chips
from card import card
from deck import deck
from hand import hand
from display import display

import random



class blackjack():
    """Class that executes the logic and calls the classes necessary to run blackjack."""
    def __init__(self):
        pass

    def play(self):
        """Function initiates the blackjack game and runs the logic"""
        # Flag to continue playing
        playing = True
        display.welcome_msg()
        # Prompt user for and set amount of chips to play with
        chips.set_total(display.prompt_chips())
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

chips = chips(500)
blackjack = blackjack()
blackjack.play()
