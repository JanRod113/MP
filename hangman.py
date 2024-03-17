# Jan Rodolfo III S. Carrillo, 221380
# March 15, 2024

# I/we certify that this submission complies with the DISCS Academic Integrity
# Policy.

# If I/we have discussed my/our Python language code with anyone other than
# my/our instructor(s), my/our groupmate(s), the teaching assistant(s),
# the extent of each discussion has been clearly noted along with a proper
# citation in the comments of my/our program.

# If any Python language code or documentation used in my/our program
# was obtained from another source, either modified or unmodified, such as a
# textbook, website, or another individual, the extent of its use has been
# clearly noted along with a proper citation in the comments of my/our program.

################################################################################

# Amar, Rameses, CS in Game Development, DLSU - L (consulted for creating the functions
# in this program)

################################################################################

# your python code starts here

# Prints the introductory messages of the hangman game with a reference to the movie, "Saw"
print("I WANT TO PLAY A GAME")
print("LET'S PLAY HANGMAN!")

# Initializes the variable with the word to be guessed by the player. For this game, I made the player
# guess the name of this cute girl I like
guess_the_word = "CHESKA".upper()

# Initializes "word" as a list of dashes representing the length of the word to be guessed
word = ['-'] * len(guess_the_word)

# List that stores all uppercase letters in the english alphabet
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Number of guesses that the player has. Synonymous to that of the actual game.
remaining_guesses = 6


# The print_word Function that takes three parameters to represent the current state of the word
# remaining guesses, and unused letters from alphabet
def print_word(word, guesses_left, unused_letters):
    word_string = ""  # Initialize an empty string to store the word representation
    for letter in word:  # creates a for loop that goes through each letter in the word list
        word_string += letter + " "  # Concatenate each letter plus space to word_string
    if word_string:  # if statement checks whether word_string is empty or not
        word_string = word_string[:-1]  # If not empty, removes last space from word_string

    unused_letters_string = ""  # Initialize an empty string to represent unused letters
    for letter in unused_letters:  # creates for loop that goes through each letter in the unused_letters list
        unused_letters_string += letter  # Concatenates each letter to unused_letters_string

    # Prints a message for the word with guesses left and unused letters
    print("Guess the word, " + str(guesses_left) + " guesses left: " + word_string)
    print("Unused letters:", unused_letters_string)


# The current_state_word Function takes three parameters that represent the current state of the word to guess,
# the actual word, and the letter guessed by the player
def current_state_word(word_to_guess, secret_word, letter):
    i = 0  # initializes the variable i at index 0
    while i < len(secret_word):  # loops through each index of the word to be guessed

        # if letter guessed is inside the word to be guessed, updates the corresponding index in the word_to_guess list
        if secret_word[i] == letter:
            word_to_guess[i] = letter
        i += 1


# calls the print_word function to start the initial state of the game
print_word(word, remaining_guesses, alphabet)

# Creates a while loop that continues infinitely so long as there are dashes in 'word' and the
#  player has remaining guesses
while '-' in word and remaining_guesses > 0:
    guess = input().upper()  # Asks a letter as input from the player and converts it to uppercase

    i = 0  # initializes the variable i at index 0
    while i < len(guess_the_word):  # creates a while loop that goes through each character of the word to be guessed
        if guess_the_word[i] == guess:  # If the guessed letter is found in the word, loop breaks
            break
        i += 1
    else:  # take a cut from the remaining guesses if the guessed letter is not in the word
        remaining_guesses -= 1

    alphabet.remove(guess)  # Removes guessed letter from the alphabet list
    current_state_word(word, guess_the_word, guess)  # Updates the current state of the word
    print_word(word, remaining_guesses, alphabet)  # Prints current state of game

# if statement checks if game is won. If yes, displays congratulatory message. If not, hangs the player
if '-' not in word:
    print("CONGRATULATIONS! YOU WIN!")
else:
    print("SORRY, YOU ARE HANGED!")
