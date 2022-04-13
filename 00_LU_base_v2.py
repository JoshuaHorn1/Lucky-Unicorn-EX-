"""LU base component - based on 00_LU_base_v1
components added after they have been created and tested
"""
import random

# yes/no checking function:
def yes_no(question_text):
    while True:

        # Ask the user if they have played before
        answer = input(question_text).lower()

        # if they say yes, output 'program continues'
        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer

        # if they say no, output 'display instructions'
        elif answer == "no" or answer == "n":
            answer = "No"
            return answer

        # otherwise - show error
        else:
            print("Please answer 'Yes (Y)' or 'No (N)'")


# Function to display instructions
def instructions():
    print("***** How to Play *****")
    print()
    print("The rules of the game will go here")
    print()


# num check function
def num_check(question, low, high):
    error = "That was not a valid input\n" \
            "Please enter a number between {} and {}\n".format(low, high)

    # keep asking until a valid amount (1-10) is entered
    while True:
        try:
            # ask for
            response = int(input(question))

            # check for number within range
            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# token generating function
def generate_token(balance):

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
        print()
        print(f"Round {rounds_played}. token: {token}, Balance: ${balance:.2f}")
        print()
        if balance < 1:
            print("\nSorry but you have fun out of money")
            print()
            play_again = "x"
        else:
            play_again = input("Do you want to play another round?\n"
                               "<enter> to play again or 'x' to exit: ").lower()  # asks the user if they want to play another round or stop
    return balance


# Main routine goes here...
played_before = yes_no("Have you played this game before?: ")

if played_before == "No":
    print(instructions())

# ask the user how much they want to play with
starting_balance = num_check("How much would you like to play with? $: ", 1, 10)
print(f"You are playing with ${starting_balance}!")

closing_balance = generate_token(starting_balance)
print("Thanks for playing!\n"
      f"You started with ${starting_balance:.2f}\n"  # (.2f) turns balance into 2 decimal places
      f"and leave with ${closing_balance:.2f}\n"
      f"Goodbye!")
