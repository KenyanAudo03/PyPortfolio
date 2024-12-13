from calendar import *

year = input("Enter Year: ")
if year:
    if len(year) == 4:
        print(calendar(int(year), 2, 0, 8, 3))
    elif len(year) < 4:
        print("A year contains 4 value of numbers")
    else:
        print("A year can't contain more than 4 values of number")

else:
    print("please enter a value")
    year = input("Enter Year: ")