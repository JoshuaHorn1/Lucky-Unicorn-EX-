"""Component 2 (How much) v2
use a try/accept and pull error message out of the loop
"""

def num_check(question, low, high):
    error = "That was not a valid input\n"
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


# main routine...
user_balance = num_check("How much would you like to play with? $: ", 1, 10)
print(f"You are playing with ${user_balance}!")
