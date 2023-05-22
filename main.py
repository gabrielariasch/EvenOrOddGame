print("Welcome to the Odd - Even Detector!")

game_on = True

while game_on:
    number = int(input("Please enter a number: "))
    
    if number % 2 == 0:
        print("The number is even!")
    else:
        print("The number is odd!")

    response = input("Do you want to keep playing? Y/N: ")
    if response == 'Y':
        game_on
    else:
        game_on = False
        print("Thanks for playing!")
        break