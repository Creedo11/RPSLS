from player import Player:
import random

class AI(Player):
    def __init__(self, name):
        super().__init__()
        self.name = name 
        self.score = 0

    def choose_gesture(self):
        gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        self.chosen_gesture = str(random.randint(0,4))
        print(f"{self.name} Has picked {gesture_list[int(self.choose_gesture)]}")


