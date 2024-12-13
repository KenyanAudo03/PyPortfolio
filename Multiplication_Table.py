from colorama import Fore
number1 = int(input("Enter the number table: "))
for num in range(1, 24):
    print(Fore.GREEN , number1, "*",num , "=", number1*num)
print(Fore.WHITE)