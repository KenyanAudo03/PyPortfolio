
# #Lists
# print("Lists")
# items = []
# items.extend(["John", "Sarah"])
# items.extend(["Peter"])
# items.sort(key=str.lower)
# print(items)

# print('')
# #Tuples cannot be alteredfied
# print("Tuple")
# names = ("John", "Syd")
# print(sorted(names) )
# newTuple = names + ("Peter", "James")
# print(newTuple)

# print('')
# #Dictionaries
# print("Dictionaries")
# players = ['Peter', "John", "Manuel"]
# coaches = ["Lenox", "Purity"]

# dic = {"To_play": players, "To_coatch": coaches}
# print(f'Palyers are: {dic.pop("To_play")} \nCoatches are: {dic.pop("To_coatch")}')

# print('')
# #Sets
# print("Sets")
# set1 = {"James", "John", "Peter"}
# set2 = {"James"}
# intersect = set1 & set2
# print(f'Common Value in the Sets: {intersect}')
# union = set1 | set2
# print(f'Union of the Sets: {union}')
# differnce = set1 - set2
# print(f'Differences of the Sets: {differnce}') 

# print('')
# #functions
# print("Functions")
# def hello(name, age):
#     print(f'Hello {name} You are {age}')
# hello(age = 19 , name = "John")

# print('')
# #For each loop in strings
# print("For each loop in string")
# phrase = "I am going to buy milk"
# words = phrase.split(' ')
# for word in words:
#     print(word)

# print('')
# #For loop in numbers
# print("For loop in numbers")
# numbers = [1, 2, 3, 4, 5]
# for index, number in enumerate(numbers):
#     print(number, index)

 
# count = 0
# while count < 10:
#     print("Hello World")
#     count += 1 

# print('')
# #Lambda Functons
# print("Lambda")
# Multiplication= lambda a, b : a * b
# print(Multiplication(2, 4))
# print('')

# #Map
# print("Map")
# numbers = [1, 2, 3]
# double = lambda a : a * 2
# result = map(double, numbers)
# print(list(result)) 
# print('')

# #Filter
# print('Filter')
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# even = lambda n : n % 2 == 0
# result = filter(even, numbers)
# print(list(result))
# print('')
# #Add items
# print('Adding Items in a list ')
# values = [20, 10, 50]
# sum = 0
# for value in values:
#     sum += value
# print(sum)
# print('')

# #Recursion
# print("Recursion (Factorial)")
# def Factorial(n):
#     if n == 1: return 1
#     return n * Factorial(n - 1)
# print(Factorial(5))
# print('')

# #Decorators
# print('Decorators')
# def longtime(func):
#     def wrapper():
#         print('before')
#         val = func()
#         print('after')
#         return val
#     return wrapper

# @longtime
# def hello():
#     print('hello')
# hello()
# print('') 

# #List conversion
# print('List convertion')
# numbers = [1, 2, 3, 4, 5 ]
# numbers_pow_2 = [n**2 for n in numbers]
# print(numbers_pow_2)
# print(' ')


# name = input("Your name: ")
# year_of_birth = int(input("Enter your year of birth: "))
# current_year = int(input("Enter current year: "))

# age = current_year - year_of_birth

# print(f'{name} your age is {age}')

# import math

# b = float(input("Enter height: "))
# c = float(input("Enter length: "))
# a = float(math.sqrt(b**2 + c**2))
# print(f'Hypothenius: {a}')

# Temperature = 87

# if Temperature >= 87:
#     print("1")
# elif Temperature == 87:
#     print("2")

# a = '2'
# b = '2'
# print(a + b)
# num = [1, 2, 3, 4, 5]

# numbers_pow_2 = [n**2 for n in num]
# print(numbers_pow_2)


# from colorama import Fore
# names = []
# names.extend(["John", "Peter", "Samwel", "Victor"])
# print("Users in the List are: ")

# count = 0
# for i in names:
#     count += 1
#     print(Fore.BLUE+f'{count}.{i}')
# print(Fore.WHITE)


# if names not in names:
#     count = float(input("How many users do you want to add? "))
#     while count > 0:
#         names.append(input("Name: "))
#         count -=1
# print()
# print("New list:")
# count = 0
# for i in names:
#     count +=1
#     print(Fore.CYAN+f'{count}.{i}'+Fore.WHITE)

# number = float(input("Enter a number: "))

# if number == 0:
#     print("Zero")
# elif number > 0:
#     print("Positive")
# else:
#     print("Negative")

# list = ["John", "Peter", "Juma", "Kerry", "James", "Joshua"]

# print(len(list))
# print()
# count = 0
# for i in list:
#     count += 1
#     print(f'{count}.{i}')


numbers = [1, 2, 3, 4, 5]
total = 0
for number in numbers:
    total += number
print(total)