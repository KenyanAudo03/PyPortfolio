import sys
from random import choice
from colorama import Fore

choices = ['rock', 'paper', 'scissors']

def bot(your_choice, bot_score, player_score):
    bot_choice = choice(choices)
    print(f'Bot Choice: {bot_choice}')

    if your_choice == "1" and bot_choice == choices[1] or \
            your_choice == "2" and bot_choice == choices[2] or \
                your_choice == "3" and bot_choice == choices[0]:
        print(Fore.RED + 'You Lose')
        print(Fore.WHITE + '')
        bot_score += 1

    elif your_choice == "1" and bot_choice == choices[0] or \
           your_choice == "2" and bot_choice == choices[1] or \
              your_choice == "3" and bot_choice == choices[2]:
        print(Fore.BLUE + "You Tie")
        print(Fore.WHITE + '')
    
    elif your_choice == "1" and bot_choice == choices[2] or \
           your_choice == "2" and bot_choice == choices[0] or \
              your_choice == "3" and bot_choice == choices[1]:
        print(Fore.YELLOW + 'You win')
        print(Fore.WHITE + '')
        player_score += 1
    
    return bot_score, player_score

def display_score(bot_score, player_score):
    print(Fore.LIGHTMAGENTA_EX + f'Bot score: {bot_score} | Player Score: {player_score}')
    print(Fore.WHITE + '')

def player_input(your_choice, bot_score, player_score):
    if your_choice in ['1', '2', '3']:
        print(f'You choose {choices[int(your_choice) - 1].upper()}')
        bot_score, player_score = bot(your_choice, bot_score, player_score)
    elif your_choice == "4":
        display_score(bot_score, player_score)
    elif your_choice == "5":
        sys.exit()
    else:
        print(Fore.RED + "Invalid Choice.....Retry")
        print(Fore.WHITE + "")
        
    return bot_score, player_score

def main():
    bot_score = 0
    player_score = 0

    while True:
        print("Choose")
        print('1.Rock \n'
              '2.Paper \n'
              '3.Scissors \n'
              '4.Display Score \n'
              '5.Exit')
        your_choice = input("Choice: ")
        print('')

        bot_score, player_score = player_input(your_choice, bot_score, player_score)

        if bot_score == 10 or player_score == 10:
            if bot_score > player_score:
                print(Fore.GREEN + "Bot Wins!")
            elif bot_score < player_score:
                print(Fore.GREEN + "Player Wins!")
            else:
                print(Fore.BLUE + "It's a Tie!")
            display_score(bot_score, player_score)
            sys.exit()

if __name__ == '__main__':
    print('WELCOME TO ROCK PAPER SCISSORS GAME')
    main()


