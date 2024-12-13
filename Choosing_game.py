import random

def get_choice():
    player_choice = input("Enter a choice(rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:
        return "It's a Tie"
    elif player == "paper":
        if computer == "rock":
            return "Paper covered Rock. You win!"
        else:
            return "Scissors cuts Paper. You lose"
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cuts Paper. You win!"
        else:
            return "Rock Smashes Scissors. You lose"
    elif player == "rock":
        if computer == "paper":
            return "Rock smashes scissors. You win!"
        else:
            return "Paper covers Paper. You lose"

choices = get_choice()
result = check_win(choices["player"], choices["computer"])
print(result)
        
