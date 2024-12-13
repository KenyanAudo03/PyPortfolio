car_started = False
car_stopped = False
print("Welcome to the Car game")
print("enter 'help' to get help")

while True:
    command = input("> ").lower()
    if command == "quit":
        print("Game Over")
        break
    elif command == "start":
        if car_started:
            print("Car already started")
        else:
            print("Car started")
            car_started = True
            car_stopped = False
    elif command == "stop":
        if car_stopped:
            print("Car already stopped")
        else:
            print("Car stopped")
            car_stopped = True
            car_started = False
    elif command == "help":
        print('''
                  start - start the car.
                  stop  - stop the car.
                  quit - quit the game.''')
    else:
        print("Unknown Command")