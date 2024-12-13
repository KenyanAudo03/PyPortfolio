from colorama import Fore
def welcome_note():
    text = "Welcome to my calculator!!!"
    print(text.upper())

def simple_arithemetic():
    print("Enter number1 and number2 then follow the steps")
    num1 = float(input("Enter number1: "))
    num2 = float(input("Enter number2: "))

    operation = int(input('''
         Types of Operation Involved:
            1.Additon.
            2.Subtraction.
            3.Multiplication.
            4.Division.
        Choose an Operation (1,2,3,4): '''))
    if operation == 1:
        ans = num1 + num2
        print(Fore.BLUE + f'Answer = {ans}')
        print(Fore.WHITE +'')
    elif operation == 2:
        ans = num1 - num2
        print(Fore.BLUE + f'Answer = {ans}')
        print(Fore.WHITE +'')
    elif operation == 3:
        ans = num1 * num2
        print(Fore.BLUE + f'Answer = {ans}')
        print(Fore.WHITE +'')
    elif operation == 4:
        ans = num1 / num2
        print(Fore.BLUE + f'Answer = {ans}')
        print(Fore.WHITE +'')
    else:
        print(Fore.RED + "Invalid Choice")
        print(Fore.WHITE + '')
while True:
  simple_arithemetic()