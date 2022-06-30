from player import Player
import time 

class Human(Player):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.score = 0  

    def choose_gesture(self):
        print("Choose 0 for Rock\n" "Choose 1 for Paper\n" "Choose 2 for Scissors\n" "Choose 3 for Lizard\n" "Choose 4 for Spock\n")
        print(" ")
        time.sleep(1)
        user_choice = input(f"{self.name}, choose your gesture: ")
        time.sleep(1)
        print(" ")
        self.chosen_gesture = user_choice
        if user_choice == "0":
            self.chosen_gesture = "Rock"
            print(f"{self.name} has chosen {self.chosen_gesture}")
            time.sleep(1)
            print(" ")
        elif user_choice == "1":
            self.chosen_gesture = "Paper"
            print(f"{self.name} has chosen {self.chosen_gesture}")
            time.sleep(1)
            print(" ")
        elif user_choice == "2":
            self.chosen_gesture = "Scissors"
            print(f"{self.name} has chosen {self.chosen_gesture}")
            print(" ")
        elif user_choice == "3":
            self.chosen_gesture = "Lizard"
            print(f"{self.name} has chosen {self.chosen_gesture}")
            time.sleep(1)
            print(" ")
        elif user_choice == "4":
            self.chosen_gesture = "Spock"
            print(f"{self.name} has chosen {self.chosen_gesture}")
            time.sleep(1)
            print(" ")
        else:
            print("Incorret input, please try again. ")
            time.sleep(1)
            print(" ")
            self.choose_gesture()



