x = int(input("what is the wind speed in MPH\n>"))

if x<74:
    print("It is a tropical storm")

elif x<96 :
    print("It is a CAT 1 hurricane")

elif x<111 :
    print("It is a CAT 2 hurricane")

elif x<130 :
    print("It is a CAT 3 hurricane")

elif x<157 :
    print("It is a CAT 4 hurricane")

elif x>=157 :
    print ("It is a Cat 5 Hurricane")