import random

def hangman():
    print("Welcome to Hangman!")
    
    # List of words to choose from
    word_list = ['python', 'hangman', 'computer', 'programming', 'developer', 'keyboard']
    
    # Randomly select a word
    word_to_guess = random.choice(word_list)
    
    # Initialize the hidden word with underscores
    hidden_word = ['_'] * len(word_to_guess)
    
    # Number of allowed attempts
    attempts_left = 6
    guessed_letters = set()
    
    print("The word to guess has", len(word_to_guess), "letters.")
    
    while attempts_left > 0:
        print("\nCurrent word:", " ".join(hidden_word))
        print("Guessed letters:", ", ".join(sorted(guessed_letters)))
        print(f"You have {attempts_left} attempts left.")
        
        # Take the player's guess
        guess = input("Enter a letter: ").lower()
        
        # Check if the input is a valid letter
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter!")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word_to_guess:
            print(f"Good guess! The letter '{guess}' is in the word.")
            # Update the hidden word with the guessed letter
            for i in range(len(word_to_guess)):
                if word_to_guess[i] == guess:
                    hidden_word[i] = guess
        else:
            attempts_left -= 1
            print(f"Oops! The letter '{guess}' is not in the word.")
        
        # Check if the player has guessed the entire word
        if ''.join(hidden_word) == word_to_guess:
            print("\nCongratulations! You've guessed the word:", word_to_guess)
            break
    else:
        print("\nYou're out of attempts! The word was:", word_to_guess)

if __name__ == "__main__":
    hangman()
