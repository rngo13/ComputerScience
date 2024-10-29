#nested if statements 
# you are a prime member or oder is at least $25
# you are at least 18 years old or have parent consent

prime = True
cost = 20
age = 17
consent = False

if prime:
    if age>=18:
        print("you are eligible for free shipping")
    elif consent:
        print("you are eligible for free shipping")
    else:
        print("you are not eligible for free shipping")

elif cost >=25:
    if age>=18:
        print("you are eligible for free shipping")
    elif consent:
        print("you are eligible for freee shipping")
    else:
        print("you are not eligible for free shipping")

else:
    print("you are not eligible for free shipping")




# do we need an umbrella 

# we need an umbrela if it is raining and we are outside
raining= True
outside = True

if raining and outside:
    print("bring an umbrella")

else:
    print("dont bring an umbrella")




if raining:
    if outside:
        print("bring an umbrella")
    else:
        print("dont bring an umbrella")



raining=input("is it raining today?")

if raining.lower()=="yes" :
    outside = input("are you going outside today")
   
    if outside.lower() == "yes" :
        print("dont bring an umbrella")
    else:
        print("dont bring an umbrella")

else:
    print("dont bring an umbrella")