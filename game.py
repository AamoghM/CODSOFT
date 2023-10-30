import random

player_choice = input("Welcome to Rock, Paper or Scissors. Enter your choice: ").strip().lower()
possible_actions = ["rock", "paper", "scissors"]
computer_choice = random.choice(possible_actions)
print(f"\nYou chose {player_choice}, computer chose {computer_choice}.\n")

if player_choice == computer_choice:
    print(f"Both players selected {player_choice}. It's a tie!")
elif player_choice == "rock":
    if computer_choice == "scissors":
        print("You win!")
    else:
        print("You lose.")
elif player_choice == "paper":
    if computer_choice == "rock":
        print("You win!")
    else:
        print("You lose.")
elif player_choice == "scissors":
    if computer_choice == "paper":
        print("You win!")
    else:
        print("You lose.")