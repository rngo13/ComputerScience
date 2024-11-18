import random

number = str(random.randint(1,100))

user_input=""

attempts=0

while user_input != number:
    try:
        user_input = input("guess the number\n>")
        attempts = attempts + 1
    except:
        print("hmmm thats not right")

    if user_input == number:
        print("you got it right")
        print("done in " + str(attempts) + " attempts")
    elif user_input > number:
        print("lower")
    
    elif user_input < number:
        print("higher")
