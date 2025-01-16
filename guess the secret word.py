import os
import time
def clear_console():
    """Clears the console screen."""
    os.system("cls" if os.name == "nt" else "clear")
def display_hangman(attempts):
    """Provides the hangman graphic based on remaining attempts."""
    stages = [
        """
           --------
           |      |
           |      O
           |     
           |     
           |
        """,
        """
           --------
           |      |
           |      O
           |      |
           |     
           |
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |      |
           |
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |      |
           |     /
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |      |
           |     / \\
        """,
    ]
    return stages[len(stages) - attempts - 1]
def guess_the_word():
    """Main function to run the hangman game."""
    clear_console()
    print("Welcome to the Hangman Game!\n")
    print("Player 1: Think of a word for Player 2 to guess.")

    secret_word = input("Enter the secret word: ").strip().lower()
    while not secret_word.isalpha():
        print("Invalid input! The word must contain only alphabets.")
        secret_word = input("Enter the secret word: ").strip().lower()
    clear_console()
    guessed_word = ["_" for _ in secret_word]
    guessed_letters = set()
    attempts = 5

    while attempts > 0 and "_" in guessed_word:
        print(display_hangman(attempts))
        print(f"Current word: {' '.join(guessed_word)}")
        print(f"Used letters: {', '.join(sorted(guessed_letters))}")
        print(f"Attempts left: {attempts}\n")

        guess = input("Guess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Enter a single alphabet.")
            time.sleep(1)
            clear_console()
            continue

        if guess in guessed_letters:
            print("Letter already guessed! Try another.")
            time.sleep(1)
            clear_console()
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print(f"Correct! The letter '{guess}' is in the word.")
            for index, char in enumerate(secret_word):
                if char == guess:
                    guessed_word[index] = guess
        else:
            print(f"Wrong! The letter '{guess}' is not in the word.")
            attempts -= 1

        time.sleep(1)
        clear_console()

    if "_" not in guessed_word:
        print(f"Congratulations! You guessed the word '{secret_word}'!")
    else:
        print(display_hangman(0))
        print(f"Game over! The word was: {secret_word}")
if __name__ == "__main__":
    guess_the_word()
