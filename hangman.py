import random

def get_guess(hidden_word):
    
    # Set guess amount and dashes
    dashes = "-" * len(hidden_word)
    guesses_left = 10

    # init game
    while guesses_left > -1 and not dashes == hex:

        # Prints dashes and guess left to the screen
        print(dashes)
        print(str(guesses_left))

        # User input
        guess = input("Guess:")

        # Checks if user enters more than one character or none at all
        if len(guess) != 1:
            print("One character at a time.")
        # Checks for letter match
        elif guess in hidden_word:
            print("The letter is in the secret word!")
            dashes = update_dashes(hidden_word, dashes, guess)
            # Checks if completed word matches hidden_word
            if dashes == hidden_word:
                print("You win. The secret word was: " + str(hidden_word))
                break


        else:
            print("That letter is not in the secret word!")
            guesses_left -= 1

    if guesses_left < 0:
        print("You lose. The secret word was: " + str(hidden_word))

# Updates the dashes with letters if needed
def update_dashes(hidden, dash, guess):
    result = ""

    # Finds where the letters need to be placed
    for i in range(len(hidden)):
        if hidden[i] == guess:
            result = result + guess
        else:
            result = result + dash[i]

    return result

# Word list
words = ["omega", "silent", "solitude", "hangman", "chef", "world", "expectation", "order", "intel", "amd"]

# Sets hidden word randomly
hidden_word = random.choice(words)
get_guess(hidden_word)