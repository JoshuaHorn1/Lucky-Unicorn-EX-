"""Took function from component 03_v1 as basis for this new function
which incorporates both yes/no and show instructions
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
    print("Program continues")
    print()


# Main routine goes here...
played_before = yes_no("Have you played this game before?: ")

if played_before == "No":
    print(instructions())
else:
    print("Program continues")
