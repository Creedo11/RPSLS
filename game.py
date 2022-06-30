from ai import AI
from human import Human 
import time


class Game:

    def __init__(self):
        self.player_one = None
        self.player_two = None 

    def run_game(self):
        self.print_display_welcome_rules() 
        self.choose_number_of_players()
        self.run_game_rounds()
        self.determine_winner()

        

    def print_display_welcome_rules(self):
        time.sleep(1)
        print("Welcome to Rock Paper Scissors Lizard Spock.")
        print(" ")
        time.sleep(1)
        print("Each match will be a best of three games.")
        print("Use the number keys to enter your selection.")
        print("")
        time.sleep(1.5)
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
        print("")
        time.sleep(1)


    def choose_number_of_players(self):
        user_choice = input("How many players? 1, 2 or 3 for a surprise? ")
        print(" ")
        time.sleep(1)
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
            time.sleep(1)
            self.choose_number_of_players()

  
    def run_game_rounds(self):
        while self.player_one.score < 2 and self.player_two.score < 2:
            self.player_one.choose_gesture()
            self.player_two.choose_gesture()
            if self.player_one.chosen_gesture == self.player_two.chosen_gesture:
                print("This round is a tie, please continue to the next round. ")
                time.sleep(1)
                print(" ")
            elif self.player_one.chosen_gesture == "Scissors" and (self.player_two.chosen_gesture == "Paper" or self.player_two.chosen_gesture == "Lizard"):
                print(f"{self.player_one.name} has won the round. ")
                time.sleep(1)
                print(" ")
                self.player_one.score += 1
            elif self.player_one.chosen_gesture == "Paper" and (self.player_two.chosen_gesture == "Rock" or self.player_two.chosen_gesture == "Spock"): 
                print(f"{self.player_one.name} has won the round. ")
                time.sleep(1)
                print(" ")
                self.player_one.score += 1
            elif self.player_one.chosen_gesture == "Rock" and (self.player_two.chosen_gesture == "Lizard" or self.player_two.chosen_gesture == "Scissors"):
                print(f"{self.player_one.name} has won the round. ")
                time.sleep(1)
                print(" ")
                self.player_one.score += 1
            elif self.player_one.chosen_gesture == "Lizard" and (self.player_two.chosen_gesture == "Spock" or self.player_two.chosen_gesture == "Paper"): 
                print(f"{self.player_one.name} has won the round. ")
                time.sleep(1)
                print(" ")
                self.player_one.score += 1
            elif self.player_one.chosen_gesture == "Spock" and (self.player_two.chosen_gesture == "Scissors" or self.player_two.chosen_gesture == "Rock"): 
                print(f"{self.player_one.name} has won the round. ")
                time.sleep(1)
                print(" ")
                self.player_one.score += 1
            else:
                print(f"{self.player_two.name} has won the round. ")
                time.sleep(1)
                print(" ")
                self.player_two.score += 1


    def determine_winner(self):
        if self.player_one.score == 2:
            print(f"{self.player_one.name} has won 2 out of 3 rounds and is declared the winner! ")
            time.sleep(1)
        elif self.player_two.score == 2:
            print(f"{self.player_two.name} has won 2 out of 3 rounds and is declared the winner! ")
            time.sleep(1)

      
        
