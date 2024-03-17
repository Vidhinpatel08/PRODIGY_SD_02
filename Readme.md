# Guessing Game

This project implements a classic guessing game in Python, where the computer generates a random number and the user tries to guess it.

## Features

* The computer generates a random number between 1 and 99 (inclusive).
* The user is prompted to guess the number.
* The program provides feedback (too high or too low) after each guess.
* The number of attempts made by the user is tracked.
* Upon successful guessing, the program displays the correct answer and the number of attempts.

## Running the Game

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Vidhinpatel08/PRODIGY_SD_02.git
   ```

2. **Run the script:**

   ```bash
   python guessing_game.py  
   ```

## How to Play

1. The program will ask you to enter a valid two-digit number.
2. Enter your guess.
3. The program will tell you if your guess is too high or too low.
4. Keep guessing until you guess the correct number.
5. The program will congratulate you and display the number of attempts it took you to guess correctly.

### Additional Notes

* This code can be further enhanced by:
    * Adding input validation to ensure users enter valid two-digit numbers within the expected range (1-99).
    * Implementing difficulty levels by adjusting the range of random numbers.
    * Setting a maximum number of attempts to add an element of challenge.
* The code utilizes a `try-except` block to handle potential errors when converting user input to an integer.

##### Feel free to modify and expand upon this code to create your own customized guessing game experience!
