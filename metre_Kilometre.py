k = 1000

while True:
    try:
        meter = float(input("Enter number to be converted into KM: "))
        km = meter/k
        print(f'{meter}m is {km}km')
        break

    except:
        print()
        print("Enter numbers Only")
        