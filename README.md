# Python_Developer_Intern_

## Task 3 Hangman Game

### Python - VS Code

---

This is a simple console-based implementation of the classic Hangman game written in Python. The game is designed for two players. Player 1 thinks of a word, and Player 2 tries to guess it within a limited number of attempts.

## Features
- A fun and interactive word-guessing game.
- ASCII art graphics to display the hangman as the game progresses.
- Player-friendly interface with error handling for invalid inputs.
- Tracks used letters and remaining attempts.

## How It Works
1. **Player 1**: Think of a word for Player 2 to guess and enter it when prompted. The word must consist only of alphabets.
2. **Player 2**: Guess one letter at a time to try and reveal the secret word.
3. You have 5 attempts to guess the word. Each incorrect guess decreases the remaining attempts.
4. The game ends when:
   - The word is successfully guessed, or
   - The number of attempts runs out.

## Game Flow
1. The game clears the console for a clean interface.
2. The secret word is hidden and displayed as underscores (e.g., `_ _ _ _`).
3. Player 2 inputs a single letter as their guess:
   - If the guess is correct, the letter is revealed in the word.
   - If the guess is incorrect, an attempt is deducted.
4. The game provides feedback on each guess and displays the current state of the hangman graphic.
5. The game ends with a victory message if the word is guessed or a game-over message if attempts run out.

## Files Included
- **`main.py`**: Contains the complete Python script for the Hangman game.

## Code Walkthrough
### Functions
1. **`clear_console()`**
   - Clears the console screen for a cleaner game interface.

2. **`display_hangman(attempts)`**
   - Returns the hangman graphic based on the remaining attempts.
   - A total of 5 stages of the hangman graphic are provided.

3. **`guess_the_word()`**
   - The main function that runs the game.
   - Manages user input, validates guesses, and tracks the game state.
   - Displays appropriate messages and updates the hangman graphic and word.

### Key Points in the Code
- **Input Validation**: Ensures that Player 1 inputs a valid word and Player 2 inputs valid guesses.
- **ASCII Art**: Enhances the visual appeal by displaying the hangman in stages.
- **Game State**: Tracks guessed letters, remaining attempts, and the progress of the guessed word.

## Requirements
- Python 3.x
- A terminal or console to run the script.

## How to Run
1. Copy the script into a file named `hangman.py`.
2. Open a terminal and navigate to the directory containing the script.
3. Run the script using the command:
   ```
   python hangman.py
   ```
4. Follow the on-screen instructions to play the game.

## Example Gameplay
```
Welcome to the Hangman Game!

Player 1: Think of a word for Player 2 to guess.
Enter the secret word: python

Current word: _ _ _ _ _ _
Used letters:
Attempts left: 5

Guess a letter: p
Correct! The letter 'p' is in the word.

Current word: p _ _ _ _ _
Used letters: p
Attempts left: 5
```

## Contribution
Feel free to fork this repository, submit issues, and make pull requests to improve the game!

## License
This project is licensed under the MIT License.

