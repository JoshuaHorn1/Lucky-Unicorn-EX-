"""Yes/No checking function
based on 01_yes_no_v3
"""


# functions go here...
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


# main routine goes here...
show_instructions = yes_no("Have you played this game before?: ")
print(f"You entered '{show_instructions}'")
print()
having_fun = yes_no("Are you having fun?: ")
print(f"You entered '{having_fun}'")
