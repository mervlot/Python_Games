# Loop
#     Ask : roll dice?
#     If user enters y
#       Generate two random numbers
#       Print them
#     If user enters n
#       Print thanke you message
#       Terminate
#     Else
#       Print invalid choice
import random


class Main:
    def __init__(self):
        pass

    def play_game(self):
        while True:
            self.input = input("Roll the dice? (y/n): ")
            self.die1 = random.randint(1, 6)
            self.die2 = random.randint(1, 6)
            if self.input.lower() == "y":
                print(f"({self.die1}, {self.die2}) 🎲")
            elif self.input.lower() == "n":
                print("Thanks for playng 😃")
                break
            else:
                print("invald input!!!")
