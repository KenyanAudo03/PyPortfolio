# # import random

# # list = [1, 2, 3, 4, 5]
# # dust = []

# # while len(list):
# #     comp = random.choice(list)

# #     try:
# #         user = int(input("Enter a number: "))
# #         if user == comp:
# #             print("match")
# #             list.remove(comp)
# #             dust.append(comp)
# #             continue
# #         if len(str(user)) != 1:
# #             print("Enter only one Number.")
# #             continue
# #         if user in dust:
# #             print("Already used")
# #             continue
# #         if user not in list:
# #             print(f'{user} not in the list')
# #             continue
# #         else:
# #             print("Not a match")
# #     except ValueError as e:
# #         print(e)

# import random

# def roll_dice():
#     return random.randint(1, 6)

# def calculate_score(rolls):
#     return sum(rolls)

# def main():
#     print("Welcome to the Dice Game!")

#     num_players = int(input("Enter the number of players: "))
#     num_rounds = int(input("Enter the number of rounds: "))

#     scores = [0] * num_players 

#     for round in range(num_rounds):
#         print(f"\nRound {round+1}:")

#         for player in range(num_players):
#             input(f"\nPlayer {player+1}, press Enter to roll the dice...")
#             rolls = [roll_dice() for _ in range(3)]
#             score = calculate_score(rolls)
#             scores[player] += score

#             print(f"Player {player+1} rolled: {rolls}")
#             print(f"Player {player+1} score for this round: {score}")
#             print(f"Player {player+1} total score: {scores[player]}")

#     print("\nGame Over!")
#     print("Final scores:")

#     for player in range(num_players):
#         print(f"Player {player+1}: {scores[player]}")

# if __name__== "__main__":
#     main()



