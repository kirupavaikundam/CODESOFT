import random

def determine_winner(user_choice, computer_choice):
    # Function to determine the winner of the game based on choices
    if user_choice == computer_choice:  # If choices are the same, it's a tie
        return "It's a tie!"
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or  # User wins if they choose rock and computer chooses scissors
        (user_choice == 'scissors' and computer_choice == 'paper') or  # User wins if they choose scissors and computer chooses paper
        (user_choice == 'paper' and computer_choice == 'rock')  # User wins if they choose paper and computer chooses rock
    ):
        return "You win!"
    else:  # Otherwise, user loses
        return "You lose!"

def rock_paper_scissors_game():
    # Function to run the Rock-Paper-Scissors game
    user_score = 0  # Initialize user's score
    computer_score = 0  # Initialize computer's score

    print("Welcome to Rock-Paper-Scissors Game!")

    while True:  # Continue playing until the user chooses to quit
        print("\nChoose: rock, paper, scissors")
        user_choice = input("Your choice: ").lower()  # Get user's choice

        if user_choice not in ['rock', 'paper', 'scissors']:  # If user's choice is not valid
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(['rock', 'paper', 'scissors'])  # Generate computer's choice randomly

        print(f"\nYour choice: {user_choice}")  # Display user's choice
        print(f"Computer's choice: {computer_choice}")  # Display computer's choice

        result = determine_winner(user_choice, computer_choice)  # Determine the winner
        print(f"Result: {result}")  # Display the result

        if result == "You win!":  # If user wins
            user_score += 1  # Increment user's score
        elif result == "You lose!":  # If user loses
            computer_score += 1  # Increment computer's score

        print(f"Score - You: {user_score}, Computer: {computer_score}")  # Display scores

        play_again = input("Do you want to play again? (yes/no): ").lower()  # Ask if the user wants to play again
        if play_again != 'yes':  # If the user doesn't want to play again
            print("Thanks for playing! Goodbye!")
            break  # Exit the game loop

if __name__ == "__main__":
    rock_paper_scissors_game()  # Start the game if the script is run directly
