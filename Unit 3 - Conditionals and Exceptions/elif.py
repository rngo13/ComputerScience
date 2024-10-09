x = 5

if x > 0 :  # > < == >= <= !=
    print("x is a positive number")


elif x < 0:     # elif statments are always paired to an if 
    print("x is a negative number")



else:       # else statements are always paired to an if statement
            #else statements never take a condition
    print("x is a zero")


color = input("what color is the light")


if color.lower() == "green":        #only one if
    print ("go")


elif color.lower()=="red" :         # no limit to how elifs you can use
    print("stop")

elif color.lower()=="yellow":
    print("stop if you can")


else:                               #only one else
    print ("call the police")





#why do i even need elif statements???
#ccant i jsut use more if's

x = 10

if x>5:
    print("x is greater than five")


if x>8:
    print("x is greater than eight")

#######################

if x>5:
    print("x is greater than five")


elif x>8:
    print("x is greater than eight")
