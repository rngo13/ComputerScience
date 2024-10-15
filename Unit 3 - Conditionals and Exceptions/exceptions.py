#exception handling
# write a program that asks for 2 number and adds them,

#if = try
# elif = except specific error type 
#else = except
def divide_two_numbers():
    try:
        x = int(input("whats the first number?\n>"))
        y = int(input("whats the second number\n>"))
        print(x / y)
    except ValueError:
        print("please enter a number...")
        divide_two_numbers()
    
    except ZeroDivisionError:
        print("cannot divide a zero...")
        divide_two_numbers()

    finally:
        print()


divide_two_numbers()
