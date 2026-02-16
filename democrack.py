# WARNING
# THIS IS FOR EDUCATIONAL PURPOSES ONLY
# I AM NOT RESPONSIBLE FOR HOW YOU USE THIS
# ver 1.1
# normal file
# im warning you, dont delete random shit

import itertools
import sys
import string

print("Starting by trying common passes...")

# -----------------------------
# CONFIG
# -----------------------------
CHARACTERS = string.ascii_letters
MIN_LENGTH = 1
MAX_LENGTH = 10
PROGRESS_INTERVAL = 10_000_000

amtnotit = 0

# -----------------------------
# 0. Read actual password
# -----------------------------
try:
    with open('pass.txt', 'r') as file:
        actual_password = file.readline().strip()
        actual_tuple = tuple(actual_password)  # Convert once for fast comparison
except FileNotFoundError:
    print("Error: pass.txt not found. Cannot continue.")
    print("(Maybe you dont have it loaded, or you are on an online compiler that doesnt let you import it)")
    sys.exit(1)

# -----------------------------
# 1. Check common passwords first
# -----------------------------
try:
    with open('commons.txt', 'r') as commons:
        for line in commons:
            guess = line.strip()
            if guess == actual_password:
                amtnotit += 1
                print(f"Got it from commons! Password is: {guess}")
                print(f"Took {amtnotit} tries!")
                sys.exit(0)

            amtnotit += 1

            if amtnotit % PROGRESS_INTERVAL == 0:
                print(f"Tried {amtnotit} guesses so far...")

except FileNotFoundError:
    print("commons.txt not found, skipping common password check.")

# -----------------------------
# 2. Brute-force
# -----------------------------
print("Wasn't in common passes we had...")
print("Starting brute forcing...")

found = False

# Local variable speed boost
chars = CHARACTERS
product = itertools.product
actual = actual_tuple

for length in range(MIN_LENGTH, MAX_LENGTH + 1):
    for guess in product(chars, repeat=length):

        # Direct tuple comparison (no string creation)
        if guess == actual:
            amtnotit += 1
            print(f"Got it! Password is: {''.join(guess)}")
            print(f"Took {amtnotit} tries!")
            found = True
            break

        amtnotit += 1

        if amtnotit % PROGRESS_INTERVAL == 0:
            print(f"Tried {amtnotit} guesses so far...")

    if found:
        break

if not found:
    print("\nPassword was not found in the brute-force search space.")
    print("Maybe it's too long, contains numbers, symbols, or uses unsupported characters.")
    print("Perhaps read the instructions next time?")

# Reminder:
# You can remove amtnotit and the progress check entirely for slightly better speed,
# but you won't see progress updates.
