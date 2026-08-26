import random

name = input("What is your name? ")
words = [
    'volcano', 'anime', 'hotwheels', 'chess', 'peacock',
    'panda', 'physics', 'business', 'health', 'tajmahal',
    'market', 'building', 'monster', 'clown', 'amazon',
]

# tell system to choose a random word
word = random.choice(words)

print("\nGuess the characters")

# to havea guessed characters
guesses = ''
turns = 12

while turns > 0:

    failed = 0

    # show guessed characters and hidden letters
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1

    print()

    # check for gussed word
    if failed == 0:
        print("You Win")
        print("The word is:", word)
        break

    # user input
    guess = input("Guess a character: ").lower()

    # check input length
    if len(guess) != 1:
        print("Please enter a single character.")
        continue

    # check for duplicate guess
    if guess in guesses:
        print("You already guessed that character.")
        continue

    guesses += guess

    if guess not in word:
        turns -= 1
        print("Wrong")
        print("You have", turns, "more guesses")

        if turns == 0:
            print("You Lose")
            print("The word was:", word)