shopping_list = []
shopping_list.extend(["Apples", "Milk", "Bread", "Eggs", "Cheese"])
print(shopping_list)
print('')

if " " not in shopping_list:
    count = 5
    while count > 0:
        shopping_list.append(input("Add an item in the list: "))
        count -= 1


print(shopping_list)


# import numpy as np
# A = np.array([1, 2, 4])
# B = np.array([4, 5, 6])
# C = np.cross(A, B)

# print(C.sum())