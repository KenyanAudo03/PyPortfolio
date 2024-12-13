n = int(input("Enter number for series: "))

a = 0
b = 1

if n <= 0:
    print("enter valid number (>0)")
elif n == 1:
    print(a)
elif n==2:
    print(a,b)
else:
    print(a, end=" ")
    print(b, end=" ")
    i = 0
    while i < n-2:
        c = a - b
        a=b
        b=c
        print(c, end=" ")
        i+=1