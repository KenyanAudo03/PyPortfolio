def calculate_total(*args):
    total = 0
    for num in args:
        total += num
    return total
def calculate_average(*args):
    total = calculate_total(*args)
    return total / len(args)

number = [1,2,3,4,5,6,7,8,9]
result1 = calculate_total(*number)
result2 = calculate_average(*number)

print(f'Total = {result1}')
print(f'Average = {result2}')