while True:
    import time
    import random

    constant =  "K"
    letters = ["A", "B", "C", "D", "E", "F", "G", "H","I", "J","K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W","X", "Y", "Z"]
    letter1 = random.choice(letters)
    letter2 = random.choice(letters)
    letter3 = random.choice(letters)
    number1 = random.randint(0,9)
    number2 = random.randint(0,9)
    number3 = random.randint(0,9)

    number_plate = f"{constant}{letter1}{letter2}{number1}{number2}{number3}{letter3}"

    print(number_plate)
    time.sleep(0.4)


