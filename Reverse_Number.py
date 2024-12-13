num = int(input("Enter a number to be reversed: "))
def rev_num(num):
    rev = 0 
    while num > 0:
        reminder = num % 10
        rev = (rev * 10) + reminder
        num = num // 10
    return rev
    

print(f'Reverve of {num} is   {rev_num(num)}')
