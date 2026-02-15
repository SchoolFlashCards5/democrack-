# WARNING
# THIS IS FOR EDUCATIONAL PURPOSES ONLY
# I AM NOT RESPONSIBLE FOR HOW YOU USE THIS

import itertools
import sys
import string

# -----------------------------
# CONFIG
# -----------------------------
# You can change this to ascii_lowercase or ascii_uppercase if you want to make it only brute force uppercase or lowercase
CHARACTERS = string.ascii_letters
# change min or max length to however you want, to make min or max length of brute force/search space
MIN_LENGTH = 1
MAX_LENGTH = 10
# the number in between which attempts it will give a progress update
# like "Tried 20000000 times..."
PROGRESS_INTERVAL = 10_000_000

amtnotit = 0

# -----------------------------
# 0. Read actual password
# -----------------------------

# Reads password from txt, only first line because i left instructions there too :)
try:
    with open('pass.txt', 'r') as file:
        actual_password = file.readline().strip()
        actual_tuple = tuple(actual_password)  # Convert once for faster comparison
# error if pass.txt was not found (bad!!!)
except FileNotFoundError:
    print("Error: pass.txt not found. Cannot continue.")
    print("(Maybe you dont have it loaded, or you are on an online compiler that doesnt let you import it)")
    sys.exit(1)

# -----------------------------
# 1. Check common passwords first
# -----------------------------
try:
    # opens and tries common passes before brute forcing, to avoid unnecessary work
    with open('commons.txt', 'r') as commons:
        for line in commons:
            guess = line.strip()
            if guess == actual_password:
                print(f"Got it from commons! Password is: {guess}")
                print(f"Took {amtnotit} tries!")
                sys.exit(0)

            # adds one to amtnotit counter
            amtnotit += 1

            if amtnotit % PROGRESS_INTERVAL == 0:
                print(f"Tried {amtnotit} guesses so far...")

# skips common pass check if commons.txt was not found
except FileNotFoundError:
    print("commons.txt not found, skipping common password check.")

# -----------------------------
# 2. Brute-force
# -----------------------------
print("\nStarting brute forcing...\n")
found = False

# Local variable speed boost
chars = CHARACTERS
product = itertools.product
actual = actual_tuple

for length in range(MIN_LENGTH, MAX_LENGTH + 1):
    for guess in product(chars, repeat=length):

        # Direct tuple comparison (no string creation here) (used to use string, nolonger does for speed)
        if guess == actual:
            print(f"Got it! Password is: {''.join(guess)}")
            print(f"Took {amtnotit} tries!")
            found = True
            break

        # adds one to amtnotit counter as done before
        amtnotit += 1

        if amtnotit % PROGRESS_INTERVAL == 0:
            print(f"Tried {amtnotit} guesses so far...")

    if found:
        break

if not found:
    print("\nPassword was not found in the brute-force search space.")
    print("Maybe it's too long, contains numbers, symbols, or uses unsupported characters.")