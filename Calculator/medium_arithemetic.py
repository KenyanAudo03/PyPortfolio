import math
from colorama import Fore

def medium_arithemetic():
    print("Enter a number and follow steps to get eg.Square")
    number = float(input("Enter a number: "))
    operation = int(input('''
        Types of Operation Involved:
            1.Squre.
            2.Cube.
            3.Squre root.
            4.Cube root.
            5.Factorial.
            6.Sine.
            7.Cosine.
            8.Tangent.
            9.Round off.
        Choose an Operation (1,2,3,4.......): '''))
    if operation == 1:
        ans = number * number
        print(Fore.BLUE + f'Squre of {number} = {ans}')
        print(Fore.WHITE + '')
    elif operation == 2:
        ans = number * number * number
        print(Fore.BLUE + f'Cube of {number} = {ans}')
        print(Fore.WHITE + '')
    elif operation == 3:
        ans = math.sqrt(number)
        print(Fore.BLUE + f'Squre root of {number} = {ans}')
        print(Fore.WHITE + '')
    elif operation == 4:
        ans = math.cbrt(number)
        print(Fore.BLUE + f'Cube root of {number} = {ans}')
        print(Fore.WHITE + '')
    elif operation == 5:
        ans = math.factorial(int(number))
        print(Fore.BLUE + f'Factorial of {number} = {ans}')
        print(Fore.WHITE + '')
    elif operation == 6:
        angle_radian = math.radians(number)
        ans = math.sin(angle_radian)
        print(Fore.BLUE + f'Sin {number} = {ans}')
        print(Fore.WHITE + '')
    elif operation == 7:
        angle_radian = math.radians(number)
        ans = math.cos(angle_radian)
        print(Fore.BLUE + f'Cos {number} = {ans}')
        print(Fore.WHITE + '')
    elif operation == 8:
        angle_radian = math.radians(number)
        ans = math.tan(angle_radian)
        print(Fore.BLUE + f'Tan {number} = {ans}')
        print(Fore.WHITE + '')
    elif operation == 9:
        ans = round(number)
        print(Fore.BLUE + f'Round off of {number} = {ans}')
        print(Fore.WHITE + '')
    else:
        print(Fore.RED + 'Invalid choice')
        print(Fore.WHITE + '')

while True:
   medium_arithemetic()
        


