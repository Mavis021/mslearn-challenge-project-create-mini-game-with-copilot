import random

# a function that takes in users choice for string value rock, paper, sicssors. The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option.
def get_user_choice():
    user_choice = input("rock, paper, or scissors? ")
    if user_choice in ["rock", "paper", "scissors"]:
        return user_choice
    else:
        print("Invalid option. Please try again.")
        return get_user_choice()

# a function that randomly selects one of the three options rock, paper, or scissors for the computer.
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

# a function that takes in the user's choice and the computer's choice and determines the winner of the game.
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"
    
# a function that runs the game by getting the user's choice, the computer's choice, determining the winner, and printing the result. By the end of each game, the player should be asked if they want to play again. If they say yes, display the score and the game should run again from the beginning, if they say no, the game should end.
def play_game():
    user_score = 0
    computer_score = 0
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"Your choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1
        print(f"Score: You {user_score} - Computer {computer_score}")
        play_again = input("Do you want to play again? (yes/no) ")
        if play_again.lower() != "yes":
            break

# a function that starts the game by calling the play_game function.    
def start_game():
    print("Welcome to Rock, Paper, Scissors!")
    play_game()
    print("Thanks for playing!")

# a conditional statement that checks if the script is being run directly and calls the start_game function if it is.
if __name__ == "__main__":
    start_game()