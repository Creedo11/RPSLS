from player import Player

class Human(Player):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.score = 0

    def choose_gesture(self):
        print("Choose 0 for Rock\n" "Choose 1 for Paper\n" "Choose 2 for Scissors\n" "Choose 3 for Lizard\n" "Choose 4 for Spock\n")
        print(" ")
        user_choice = input("Choose your gesture")
        
        
