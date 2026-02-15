# democrack!

# BIG OLD WARNING:
# THIS IS AN EDUCATION RESOURCE
# DO NOT USE IN REAL LIFE ON REAL PASSWORDS!

### Only works with ascii letters (no symbols, no numbers, no punctuation. just letters)


democrack! is a democracker in pure python.


## Why?

Boredom and freedom can commbine for the better or for the worse, and here? A little bit of a mix.

## How this silly democracker works

It first checks from its list of common passwords (commons.txt), which ironically takes up about 95% of the storage space, then begins it's brute force.

You NEED pass.txt, which, at the first line, is the password. The rest of the file is ignored by the code.

Commons.txt is entirely optional, as it is only the common passwords file that is checked before brute forcing.

It, as stated before, checks if both files exist, if commons doesn't it begins brute, if it does, it goes through commmons first, if pass.txt doesn't exist, it cannot continue, and exits with code 1.

It first goes through the commons, so it doesn't try to brute force something dumb and easy like "1234"

Also, in the config area, you can change from ascii_letters to ascii_lowercase or ascii_uppercase to only brute force uppercase or lowercase.


## Credits

Litterally just me, Nny.
