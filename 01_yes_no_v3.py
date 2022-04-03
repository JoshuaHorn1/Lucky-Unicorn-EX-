"""LU Yes / No
puts code in v2 into a loop to make testing easier
"""

show_instructions = ""
while show_instructions != "x":

    # Ask the user if they have played before
    show_instructions = input("Have you played Lucky Unicorn before? (Yes/No): ").lower()

    # if they say yes, output 'program continues'
    if show_instructions == "yes" or show_instructions == "y":
        print("Program continues")

    # if they say no, output 'display instructions'
    elif show_instructions == "no" or show_instructions == "n":
        print("Display instructions")


    # otherwise - show error
    else:
        print("Please answer 'Yes (Y)' or 'No (N)'")

    print(f"You entered '{show_instructions}'")
