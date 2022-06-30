from player import Player

class Human(Player):
    def __init__(self):
        super().__init__()
        self.score = 0

    def choose_gesture(self):
        print("Choose 0 for Rock\n" "Choose 1 for Paper\n" "Choose 2 for Scissors\n" "Choose 3 for Lizard\n" "Choose 4 for Spock\n")
        print(" ")
        user_choice = input("Choose your gesture")
        self.chosen_gesture = user_choice
        if user_choice == "0":
            self.chosen_gesture = "Rock"
        elif user_choice == "1":
            self.chosen_gesture = "Paper"
        elif user_choice == "2":
            self.chosen_gesture = "Scissors"
        elif user_choice == "3":
            self.chosen_gesture = "Lizard"
        elif user_choice == "4":
            self.chosen_gesture = "Spock"
        else:
            print("Incorret input")
            self.choose_gesture()



