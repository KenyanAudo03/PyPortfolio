num = int(input("Enter a number: "))
if num < 1:
    print(f'{num} is not a Prime number')
else:
    for i in range(2, num):
        if num % i == 0:
            print(f'{num} is not a Prime number')
            break
        else:
            print(f'{num} is a Prime number')
            break