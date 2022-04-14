"""LU base component - based on 00_LU_base_v2
adding instructions and further decorations
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
    print()
    print(formatter("*", "How to play"))
    print()
    print("Choose a starting amount to play with - must be between $1 and $10")
    print()
    print("Then press <enter> to play. You will get a random token which might "
          "be a horse, a zebra, a donkey, or a unicorn.")
    print()
    print("It costs nothing to play each round, but depending on your prize, you "
          "could win money or lose it. These are the payout amounts:\n "
          "\tUnicorn: balance increases by $4\n "
          "\tHorse or Zebra: balance decreases by $0.50\n "
          "\tDonkey: balance decreases by $1\n ")
    print("\nSee if you can avoid getting donkeys, get the unicorns, and finish with "
          "more money than you started with.\n ")

    print("*" * 100)
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
        print()
        print(formatter(".", f"Round {rounds_played}"))
        number = random.randint(1, 100)  # can only be a donkey (so only -1 each time)

        # adjust balance
        # if the random number is between 1 and 5 user gets a unicorn (+ 4)
        if 1 <= number <= 5:
            balance += 4
            print()
            print(formatter("!", "Congratulations, you got a Unicorn"))
            print()
        # if the random number is between 6 and 36 user gets a donkey (- 1)
        elif 6 <= number <= 36:
            balance -= 1
            print()
            print(formatter("D", "Unlucky, you got a Donkey"))
            print()
        # all other cases the token must be a horse or a zebra (- .50)
        else:
            # if number is even, set token to a zebra
            if number % 2 == 0:
                balance -= 0.50
                print()
                print(formatter("Z", "Unlucky, you got a Zebra"))
                print()
            # otherwise it is a horse
            else:
                balance -= 0.50
                print()
                print(formatter("H", "Unlucky, you got a Horse"))
                print()
        # output
        print(f"Balance: ${balance:.2f}")
        if balance < 1:
            print("\nSorry but you have run out of money")
            print()
            play_again = "x"
        else:
            play_again = input("Do you want to play another round?\n"
                               "<enter> to play again or 'x' to exit: ").lower()  # asks the user if they want to play another round or stop
    return balance


# text formatting function
def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


# Main routine goes here...
print(formatter("-", "Welcome to the Lucky Unicorn Game"))
print()

played_before = yes_no("Have you played this game before?: ")

if played_before == "No":
    print(instructions())

# ask the user how much they want to play with
starting_balance = num_check("How much would you like to play with? $: ", 1, 10)
print(f"You are playing with ${starting_balance}!")

closing_balance = generate_token(starting_balance)
print("Thanks for playing!\n"
      f"You started with ${starting_balance:.2f}\n"  # (.2f) turns balance into 2 decimal places
      f"and leave with ${closing_balance:.2f}\n")
print(formatter("*", "Goodbye"))

