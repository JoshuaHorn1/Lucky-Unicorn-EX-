"""Component 4 - game mechanics and looping v2
based on 06_rounds_v1
removed hard-wiring so that all tokens can be allocated (randint 1-100)
gives user feedback about number of rounds and maintains balance
test amount set for $5
"""

import random

# main routine
TEST_AMOUNT = 5
balance = TEST_AMOUNT

rounds_played = 0
play_again = ""

while play_again != "x":
    rounds_played += 1  # keep track of rounds
    number = random.randint(1, 100)  # can only be a donkey (so only -1 each time)

    # adjust balance
    # if the random number is between 1 and 5 user gets a unicorn (+ 4)
    if 1 <= number <= 5:
        token = "unicorn"
        balance += 4
    # if the random number is between 6 and 36 user gets a donkey (- 1)
    elif 6 <= number <= 36:
        token = "donkey"
        balance -= 1
    # all other cases the token must be a horse or a zebra (- .50)
    else:
        # if number is even, set token to a zebra
        if number % 2 == 0:
            token = "zebra"
            balance -= 0.50
        # otherwise it is a horse
        else:
            token = "horse"
            balance -= 0.50

    # output
    if balance <= 0:
        print("You have run out of money!\n")
        print()
        print("Thanks for playing!\n"
              f"You started with ${TEST_AMOUNT:.2f}\n"  # (.2f) turns balance into 2 decimal places
              f"and leave with ${balance:.2f}\n"
              f"Goodbye!")
        exit()

    else:
        print()
        print(f"Round {rounds_played}. token: {token}, Balance: ${balance:.2f}")
        print()
        play_again = input("Do you want to play another round?\n"
                           "<enter> to play again or 'x' to exit: ").lower()  # asks the user if they want to play another round or stop
        if play_again == "x":
            print()
            print("Thanks for playing!\n"
                  f"You started with ${TEST_AMOUNT:.2f}\n"  # (.2f) turns balance into 2 decimal places
                  f"and leave with ${balance:.2f}\n"
                  f"Goodbye!")
            exit()
