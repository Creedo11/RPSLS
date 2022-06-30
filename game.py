from ai import AI
from human import Human

class Game:

    def __init__(self):
        self.player_one = None
        self.player_two = None 

    def run_game(self):
        self.print_display_welcome_rules()
        print(" ")
        self.choose_players()
        self.run_game_mode()
        

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
            self.choose_players()


    def run_game_mode(self):
        while self.player_one.choose_gesture and self.player_two.choose_gesture:

            if self.player_one.chosen_gesture == self.player_two.chosen_gesture:
                print("This round is a tie, please continue")
            elif self.player_one.chosen_gesture == "Scissors" and (self.player_two == "Paper" or self.player_two == "Lizzard"):
                print("Player one is the winner")
                self.player_one.score += 1
            elif self.player_one.chosen_gesture == "Paper" and (self.player_two == "Rock" or self.player_two == "Spock"):
                print("Player one is the winner")
                self.player_one.score += 1
            elif self.player_one.chosen_gesture == "Rock" and (self.player_two == "Lizard" or self.player_two == "Scissors"):
                print("Player one is the winner")
                self.player_one.score += 1
            elif self.player_one.chosen_gesture == "Lizard" and (self.player_two == "Spock" or self.player_two == "Paper"):
                print("Player one is the winner")
                self.player_one.score += 1
            elif self.player_one.chosen_gesture == "Spock" and (self.player_two == "Scissors" or self.player_two == "Rock"):
                print("Player one is the winner")
                self.player_one.score += 1
            else:
                print("Player two in the winner")
                self.player_two.score += 1


