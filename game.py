from ai import AI
from human import Human

class Game:

    def __init__(self):
        self.player_one = None
        self.player_two = None 

    def run_game(self):
        self.print_display_welcome_rules()
        print(" ")
        self.choose_number_of_players()
        self.choose_number_of_players
        self.run_game_rounds()
        

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

    def choose_number_of_players(self):
        user_choice = input("How many players? 1, 2 or 3 for a surprise? ")
        print(" ")
        if user_choice == "1":
            self.player_one = Human("Player one")
            self.player_two = AI("AI")
        elif user_choice == "2":
            self.player_one = Human("Player one")
            self.player_two = Human("Player two")
        elif user_choice == "3":
            self.player_one = AI("AI one")
            self.player_two = AI("AI two")
        else:
            print("Incorrect input. Please try again.")
            self.choose_players()

    def choose_player_gestures(self):
        self.player_one.choose_gesture()
        self.player_two.choose_gesture()

    def run_game_rounds(self):
            if self.player_one.chosen_gesture == self.player_two.chosen_gesture:
                print("This round is a tie, please continue")
            elif self.player_one.chosen_gesture == "Scissors" and self.player_two.chosen_gesture == "Paper":
                print("Player one is the winner")
                self.player_one.score += 1
            elif self.player_one.chosen_gesture == "Scissors" and self.player_two.chosen_gesture == "Lizard":
                print("Player one is the winner")
                self.player_one.score += 1
            elif self.player_one.chosen_gesture == "Paper" and self.player_two.chosen_gesture == "Rock": 
                print("Player one is the winner")
                self.player_one.score += 1
            elif self.player_one.chosen_gesture == "Paper" and self.player_two.chosen_gesture == "Spock":
                print("Player one is the winner")
                self.player_one.score += 1
            elif self.player_one.chosen_gesture == "Rock" and self.player_two.chosen_gesture == "Lizard":
                print("Player one is the winner")
                self.player_one.score += 1
            elif self.player_one.chosen_gesture == "Rock" and self.player_two.chosen_gesture == "Scissors":
                print("Player one is the winner")
                self.player_one.score += 1
            elif self.player_one.chosen_gesture == "Lizard" and self.player_two.chosen_gesture == "Spock": 
                print("Player one is the winner")
                self.player_one.score += 1
            elif self.player_one.chosen_gesture == "Lizard" and self.player_two.chosen_gesture == "Paper":
                print("Player one is the winner")
                self.player_one.score += 1
            elif self.player_one.chosen_gesture == "Spock" and self.player_two.chosen_gesture == "Scissors": 
                print("Player one is the winner")
                self.player_one.score += 1
            elif self.player_one.chosen_gesture == "Spock" and self.player_two.chosen_gesture == "Rock":
                print("Player one is the winner")
                self.player_one.score += 1
            else:
                print("Player two in the winner")
                self.player_two.score += 1


    def determine_winner(self):
        if self.player_one.score >= 2:
            print(f"{self.player_one.name} is the winner! ")
        elif self.player_two.score >= 2:
            print(f"{self.player_two.name} is the winner! ")
        else: 
            self.choose_player_gestures()

