# 📘 Assignment: Hangman

## 🎯 Objective

Build a command-line Hangman game to practice string manipulation, loops, conditionals, and handling user input.

## 📝 Tasks

### 🛠️ Build the Hangman game

#### Description
Implement a playable Hangman game that selects a secret word and lets a single player guess letters until they win or run out of attempts.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list
- Show the current word progress with blanks and correctly guessed letters (e.g. `_ a _ _ m a n`)
- Accept single-letter guesses (case-insensitive) and ignore repeated guesses
- Track and display remaining incorrect attempts
- End the round with a clear win or lose message and reveal the secret word

#### Example
```text
Secret word: _ a _ _ m a n
Guess a letter: g
Incorrect! Attempts remaining: 5
Guess a letter: h
Correct! Current word: h a _ _ m a n
```


### 🛠️ Enhancements (optional)

#### Description
Add one or more optional features to improve gameplay or usability.

#### Requirements
Completed program may:

- Load words from a file (e.g. `words.txt`) or include difficulty levels
- Show ASCII art for hangman stages
- Allow full-word guesses
- Keep simple statistics (wins/losses) across sessions
