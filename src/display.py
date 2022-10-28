from chips import chips

class display:
    """Class that handles the output for the blackjack game."""
    def welcome_msg():
        """Displays welcome header."""
        print("Welcome to blackjack!\n" + double_line)
    def prompt_chips():
        """Prompt the user for how many chips they would like to start with."""
        chips = input("How many chips would you like to start with? ")
        return chips
    def out_chips(chips):
        """Print the user's chip count"""
        print(f"\nChips: {chips}\n")

# Define lines to make output easier and more consistent
double_line = "==============================================="
line = "-----------------------------------------------"