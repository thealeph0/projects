import random

# Predefined list of words
WORDS = ["python", "hangman", "computer", "programming", "loops", "functions", "conditional"]

# Function to choose a random word
def choose_word():
    return random.choice(WORDS)

# Function to display the word with guessed letters
def display_word(word, guesses):
    displayed_word = ""
    for letter in word:
        if letter in guesses:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word.strip()

# Function to get a valid letter from the user
def get_guess(guesses):
    while True:
        guess = input("Enter a letter: ").lower()
        if len(guess) == 1 and guess.isalpha() and guess not in guesses:
            return guess
        else:
            print("Invalid input. Please enter a single letter that you haven't guessed yet.")

# Main function to run the Hangman game
def hangman():
    word = choose_word()  # Randomly select a word
    guesses = []  # List to store player's guesses
    incorrect_guesses = 0
    max_incorrect = 6
    
    print("Welcome to Hangman!")
    
    # Game loop
    while incorrect_guesses < max_incorrect:
        print(display_word(word, guesses))
        print(f"You have {max_incorrect - incorrect_guesses} incorrect guesses left.")
        print(f"Guessed letters: {', '.join(guesses)}")
        
        guess = get_guess(guesses)
        guesses.append(guess)
        
        if guess in word:
            print(f"Good guess! '{guess}' is in the word.\n")
            if all(letter in guesses for letter in word):  # Check if the player has won
                print(f"Congratulations! You've guessed the word: {word}")
                break
        else:
            incorrect_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.\n")
    
    # If the loop ends and the user hasn't guessed the word
    if incorrect_guesses == max_incorrect:
        print(f"Game over! You've used all your guesses. The word was: {word}")

# Run the game
if __name__ == "__main__":
    hangman()
