from tkinter import *
import random 

def Guess_Number():
    # Generate a random number between 1 and 100
    Guess_num = random.randint(1, 100)
    attempts = 0  # Initialize the number of attempts

    # Welcome message and instructions
    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")

    # Start an infinite loop for the guessing game
    while True:
        try:
            # Prompt the user to enter their guess
            user_guess = int(input("Guess the number: "))
            attempts += 1  # Increment the attempt count

            # Provide feedback based on the user's guess
            if user_guess < Guess_num:
                print("Higher! Try again.")  # If guess is too low
            elif user_guess > Guess_num:
                print("Lower! Try again.")  # If guess is too high
            else:
                # If the guess is correct, congratulate the user and display attempts
                print(f"Congratulations! You've guessed the number {Guess_num} in {attempts} attempts.")
                break  # Exit the loop if the guess is correct
        except ValueError:
            # Handle the case where input is not a valid integer
            print("Entered something wrong. Please enter a valid number.")

# Start the guessing game
Guess_Number()
