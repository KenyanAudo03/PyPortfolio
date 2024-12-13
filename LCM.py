num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))
def lcm(num1, num2):
    if num1 > num2:
        greater = num1
    else:
        greater = num2

    while True:
        if (greater % num1 == 0) and (greater % num2 == 0 ):
            break
        greater +=1
    return greater
print(f'LCM = {lcm(num1, num2)}')