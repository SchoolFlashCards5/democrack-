# WARNING
# THIS IS FOR EDUCATIONAL PURPOSES ONLY
# I AM NOT RESPONSIBLE FOR HOW YOU USE THIS
# ver 1.2
# normal file
# im warning you, dont delete random shit

import itertools
import sys
import string

# -----------------------------
# ASCII BANNER
# -----------------------------
print(r"""
     _                                          _    _ 
  __| | ___ _ __ ___   ___   ___ _ __ __ _  ___| | _| |
 / _` |/ _ \ '_ ` _ \ / _ \ / __| '__/ _` |/ __| |/ / |
| (_| |  __/ | | | | | (_) | (__| | | (_| | (__|   <|_|
 \__,_|\___|_| |_| |_|\___/ \___|_|  \__,_|\___|_|\_(_)
""")

# -----------------------------
# CONFIG
# -----------------------------
CHARACTERS = string.ascii_letters
MIN_LENGTH = 1
MAX_LENGTH = 10
PROGRESS_INTERVAL = 10_000_000

amtnotit = 0

# -----------------------------
# 0. Choose password source
# -----------------------------
print("Choose password source:")
print("1 - Use pass.txt")
print("2 - Type password manually")

choice = input("Enter 1 or 2: ").strip()

if choice == "1":
    try:
        with open('pass.txt', 'r') as file:
            actual_password = file.readline().strip()
            actual_tuple = tuple(actual_password)
    except FileNotFoundError:
        print("ERROR: You chose pass.txt but it DOES NOT EXIST.")
        print("Load the file or choose option 2 next time.")
        sys.exit(1)

elif choice == "2":
    actual_password = input("Type the password to brute-force: ").strip()
    actual_tuple = tuple(actual_password)

else:
    print("Invalid choice. Exiting.")
    sys.exit(1)

print("Starting by trying common passes...")

# -----------------------------
# 1. Check common passwords first
# -----------------------------
try:
    with open('commons.txt', 'r') as commons:
        for line in commons:
            guess = line.strip()

            amtnotit += 1

            if guess == actual_password:
                print(f"Got it from commons! Password is: {guess}")
                print(f"Took {amtnotit} tries!")
                sys.exit(0)

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

        amtnotit += 1

        # Direct tuple comparison (no string creation)
        if guess == actual:
            print(f"Got it! Password is: {''.join(guess)}")
            print(f"Took {amtnotit} tries!")
            found = True
            break

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
