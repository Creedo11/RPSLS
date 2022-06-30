from ai import AI
from human import Human

class Game:

    def __init__(self):
        self.player_one = None
        self.player_two = None 

    def run_game(self):
        self.print_display_welcome_rules()
        

    def print_display_welcome_rules(self):
        print("Welcome to Rock Paper Scissors Lizard Spock.")
        print(" ")
        print("Each match will be a best of three games.")
        print("Use the number keys to enter your selection.")
        print("")
        print("Scissors cut Paper")
        print("Paper covers Rock")
        print("Rock crushes Lizard")
        print("Lizard poisons Spock")
        print("Spock smashes Scissors")
        print("Scissors decapitates Lizard")
        print("Lizard eats Paper")
        print("Paper disproves Spock")
        print("Spock vaporized Rock")
        print("Rock crushed Scissors")

    def choose_players(self):
        user_choice = input("How many players? 1, 2 or 3 for a surprise?")
        if user_choice == "1":
            self.player_one = Human()
            self.player_two = AI()
        elif user_choice == "2":
            self.player_one = Human()
            self.player_two = Human()
        elif user_choice == "3":
            self.player_one = AI()
            self.player_two = AI()
        else:
            print("Incorrect input. Please try again.")
            