import random
import time
from colorama import Fore
while True:
    pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 
            'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o' 'p', 'q', 'r', 's', 't', 'u',  
            'v', 'w', 'x', 'y', 'z', 'A', 'B', 
            'C', 'D', 'E', 'F', 'G', 'H', 'I',
            'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W',
            'X', 'Y', 'Z', '1', '2', '3', '4',
            '5', '6', '7', '8', '9', '0', '!',
            '@', '#', '$', '%', '^', '&','*',
            '(', ")"]

    password = ""

    for x in range(16):
        password = password + random.choice(pass1)[0]

    print('Your New Password is:\n',   Fore.RED + password)
    print(Fore.WHITE + '')
    time.sleep(0.9)
