#loop control statements
#allow you to change how loops operate
#do things like quit the loop early, skip the current loop,, and even do nothing
#break, continute, and pass

#break
#exits a loop prematurley, before it was supposed to end

#examples

bagoffruits = ["apple", "orange", "bug", "watermelon", "pear"]

for fruit in bagoffruits:
    
    if fruit=="bug":
        print("uh oh, you found a bug in the bag")
        break # the break statment exits the loop immediately and continues
    else:
        print("you ate a " + fruit)


#continue
#skips the current loop
#it does not exit the entire loop, just moves on to the next iteration

#example
orders = [15,30,35,23,100,3,10,22]

#only apply discount for orders above 20 dollars
#coupon applying program
for order in orders:
    if order < 20:
        continue #skips the rest of the loop iteration and goes to the next 
    print(str(order) + " discounted 5% to " + str(order * .95))




#pass
# does nothing
#usually used as a placeholder while writing code
#texzt adventure project

if True:
    pass


def encounter_forest():
    pass
def swim_river():
    pass
def eat_icecream():
    pass