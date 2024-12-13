s = input("Enter a String: ")

def palindrome(string):
    x = ""
    for i in string:
        x = i + x
    return x
if s == palindrome(s):
    print(f'{s} is a palindrome')
else:
    print(f'{s} is not a palindrome')