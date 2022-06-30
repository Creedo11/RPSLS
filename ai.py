from player import Player
import random

class AI(Player):
    def __init__(self, name):
        super().__init__() 
        self.name = name
        self.score = 0  

    def choose_gesture(self):
        self.chosen_gesture = random.choice(self.gesture_list)
        print(f"{self.name} has chosen {self.chosen_gesture}")





