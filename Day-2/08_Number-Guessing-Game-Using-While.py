import random

def guess_the_number():
    # 1. Generate a random target number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")

    # 2. Start the while loop for continuous guessing
    while True:
        try:
            # Get user input and convert it to an integer
            user_guess = int(input("Take a guess: "))
            attempts += 1  # Track the number of attempts
            
            # 3. Check the user's guess against the secret number
            if user_guess < secret_number:
                print("Too low! Try again.")
            elif user_guess > secret_number:
                print("Too high! Try again.")
            else:
                # The guess is correct! Break the loop to end the game
                print(f"🎉 Congratulations! You guessed the number in {attempts} attempts.")
                break
                
        except ValueError:
            # Handle non-integer inputs without breaking the loop
            print("Invalid input. Please enter a valid whole number.")

# Run the game
guess_the_number()
