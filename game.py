class Game:

    def __init__(self):
        self.ai = ()
        self.human = ()

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


