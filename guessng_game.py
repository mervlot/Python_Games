# generate a random number
# store attempts
# Loop
#     ask the user to make a guess
#     record attempts
#     if not a valid number
#       error printed
#     if guess > number
#       too low
#     if guess < number
#       too high
#     else
#       congratulate user and show results
#       terminate
import random


class Main:
    def __init__(self):
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0

    def play_game(self):
        while True:
            try:
                guess = int(input("Guess the number between 1 and 100: "))
                self.attempts += 1
                if guess < self.number_to_guess:
                    print("Too low!")
                elif guess > self.number_to_guess:
                    print("Too high!")
                else:
                    print(
                        f"Congratulations! you guessed the number with {self.attempts} attempts"
                    )
                    break
            except ValueError:
                print("Please enter a valid number")
