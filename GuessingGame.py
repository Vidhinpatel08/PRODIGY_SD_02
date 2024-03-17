#  Task 2: Guessing Game 

# - Create a program that generates a random number.
# - Challenge the user to guess the number.
# - Provide feedback (too high/too low) and track the number of attempts.
# - Display the correct answer and number of attempts upon successful guessing.
# -------------------------------------------------------------------

import random

COMPUTER_GUESS = random.randint(1,100)
USER_GUESS = -1
No_Of_Attempt = 0

while True:
    try: 
        USER_GUESS = int(input("Enter a valid two-digit number (between 1 and 99): "))
        if 1 <= USER_GUESS <= 99:
            No_Of_Attempt += 1
        else:
            print("Number out of range. Please enter a number between 1 and 99.\n")
            continue
            
    except Exception as e:
        print("Invalid input. Please enter a two-digit number.\n") 
        continue
    
    if USER_GUESS == COMPUTER_GUESS:
        print(f"\nCongratulations, you won the game! 🎉🎉\nThe correct answer was {COMPUTER_GUESS}.\nYou took {No_Of_Attempt} guesses to reach the final answer.\n")
        break
    elif USER_GUESS > COMPUTER_GUESS : 
        print("Your guess is too high. Try a lower number.")
    else :        
        print("Your guess is too low. Try a higher number.") 

    
    


