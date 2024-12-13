# # num = int(input('Enter a year: '))
# # if num % 4 == 0:
# #     if num % 100 == 0:
# #         if num % 400 == 0:
# #             print(f'{num} is a leap year')
# #         else:
# #             print(f'{num} is not a leap year')
# #     else:
# #         print(f'{num} is leap year')
# # else:
# #     print(f'{num} is not a leap year')

# if __name__ == '__main__':
#     n = int(input())
#     for i in range(1, n + 1):
#         print(i, end="")
#         if i < n:
#             print( end="")

# Read input
size_A = int(input())
set_A = set(map(int, input().split()))
num_other_sets = int(input())

# Perform mutation operations
for _ in range(num_other_sets):
    operation, length = input().split()
    other_set = set(map(int, input().split()))

    if operation == "intersection_update":
        set_A.intersection_update(other_set)
    elif operation == "update":
        set_A.update(other_set)
    elif operation == "symmetric_difference_update":
        set_A.symmetric_difference_update(other_set)
    elif operation == "difference_update":
        set_A.difference_update(other_set)

# Print the sum of elements in the final set A
print(sum(set_A))
