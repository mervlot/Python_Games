"""This is the main file for the Mervlot Shell Games version 1.0"""

import time
import sys
import dice_game as dg
import guessng_game as gg
import rock_paper_sis_game as rpsg


dgi = dg.Main()
ggi = gg.Main()
rpsgi = rpsg.Main()

print(
    "Welcome to Mervlot Shell Games version 1.0\
       type quit to exit 😎",
    end=" ",
)

while True:
    try:
        user_input = input(
            """
1. dice game
2. guessing game
3. rock paper scissors game
>>> """
        )
        if user_input == "quit":
            print("Bye Thanks for trying 😉 ", end="")
            for _ in range(5):
                sys.stdout.write(".")
                sys.stdout.flush()
                time.sleep(0.5)
            break
        elif int(user_input) == 1:
            for _ in range(5):
                sys.stdout.write(".")
                sys.stdout.flush()
                time.sleep(0.5)
            print()
            dgi.play_game()
        elif int(user_input) == 2:
            for _ in range(5):
                sys.stdout.write(".")
                sys.stdout.flush()
                time.sleep(0.5)
            print()
            ggi.play_game()
        elif int(user_input) == 3:
            for _ in range(5):
                sys.stdout.write(".")
                sys.stdout.flush()
                time.sleep(0.5)
            print()
            rpsgi.play_game()
        else:
            print("Invalid Input ", end="")
            for _ in range(5):
                sys.stdout.write(".")
                sys.stdout.flush()
                time.sleep(0.5)
            time.sleep(1)
    except ValueError:
        print("Invalid Input ", end="")
        for _ in range(5):
            sys.stdout.write(".")
            sys.stdout.flush()
            time.sleep(0.5)
        time.sleep(1)
