"""LU base component
components added after they have been created and tested
"""


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


# Main routine goes here...
played_before = yes_no("Have you played this game before?: ")

if played_before == "No":
    print(instructions())

# ask the user how much they want to play with
user_balance = num_check("How much would you like to play with? $: ", 1, 10)
print(f"You are playing with ${user_balance}!")
