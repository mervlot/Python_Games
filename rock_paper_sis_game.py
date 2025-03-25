import random


class Main:
    def __init__(self):
        self.ROCK = "r"
        self.SCISSORS = "s"
        self.PAPER = "p"
        self.emojis = {self.ROCK: "🪨", self.SCISSORS: "✂️", self.PAPER: "📃"}
        self.choices = tuple(self.emojis.keys())

    def get_user_choice(self):
        while True:
            self.user_choice = input("Rock, paper, or scissors? (r/p/s): ").lower()
            if self.user_choice in self.choices:
                return self.user_choice
            else:
                print("Invalid choice!")

    def display_choices(self, user_choice, computer_choice):
        print(f"You chose {self.emojis[user_choice]}")
        print(f"Computer chose {self.emojis[computer_choice]}")

    def determine_winner(self, user_choice, computer_choice):
        if self.user_choice == self.computer_choice:
            print("Tie!")
        elif (
            (user_choice == self.ROCK and computer_choice == self.SCISSORS)
            or (user_choice == self.SCISSORS and computer_choice == self.PAPER)
            or (user_choice == self.PAPER and computer_choice == self.ROCK)
        ):
            print("You win")
        else:
            print("You lose")

    def play_game(self):
        while True:
            self.user_choice = self.get_user_choice()

            self.computer_choice = random.choice(self.choices)

            self.display_choices(self.user_choice, self.computer_choice)

            self.determine_winner(self.user_choice, self.computer_choice)

            should_continue = input("Continue? (y/n): ").lower()
            if should_continue == "n":
                break
