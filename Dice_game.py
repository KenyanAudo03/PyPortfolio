import random
import time
from colorama import Fore

def roll_dice():
    return random.randint(1, 6)

def calculate_score(rolls):
    return sum(rolls)

def main():
    print("Welcome to the Dice Game!")

    num_players = int(input("Enter the number of players: "))
    player_names = []
    for i in range(num_players):
        name = input(f"Enter the name of Player {i+1}: ")
        player_names.append(name)

    time_limit = None
    while not time_limit:
        time_input = input("Enter the time limit for the game (in seconds): ")
        if time_input.isdigit():
            time_limit = int(time_input)
        else:
            print("Invalid input. Please enter a valid time limit.")

    scores = [0] * num_players

    start_time = time.time()
    end_time = start_time + time_limit

    round_num = 1
    while time.time() < end_time:
        print(Fore.RED + f"\nRound {round_num}:" + Fore.WHITE)

        for player in range(num_players):
            input(f"\n{player_names[player]}, press Enter to roll the dice...")
            rolls = [roll_dice() for _ in range(3)]
            score = calculate_score(rolls)
            scores[player] += score

            print(f"{player_names[player]} rolled: {rolls}")
            print(f"{player_names[player]} score for this round: {score}")
            print(f"{player_names[player]} total score: {scores[player]}")

        round_num += 1

    print("\nGame Over!")
    print("Final scores:")

    for player in range(num_players):
        print(f"{player_names[player]}: {scores[player]}")

if __name__== "__main__":
    main()