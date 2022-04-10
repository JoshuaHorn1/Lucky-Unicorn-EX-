"""Component 3 (random tokens) v4
calculate persentages to ensure the odds favour the house
5% unicorns, 30% donkeys, and the remaining 65% horses/zebras
"""

import random


STARTING_BALANCE = 100
balance = STARTING_BALANCE

# testing loop to generate 100 tokens
for item in range(10):
    number = random.randint(1, 100)

    # adjust balance
    # if the random number is between 1 and 5 user gets a unicorn (+ 4)
    if 1 <= number <= 5:
        token = "unicorn"
        balance += 4
    # if the random number is between 6 and 36 user gets a donkey (- 1)
    elif 6 == number <= 36:
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
    print(f"token: {token}, Balance: ${balance:.2f}")

print()
print(f"Starting balance = ${STARTING_BALANCE:.2f}")
print(f"Final balance = ${balance:.2f}")
