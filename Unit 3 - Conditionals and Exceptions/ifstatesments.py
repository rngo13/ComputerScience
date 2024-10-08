# if statemnts evaluate boolean expressions
# make decisions about which code to run next

#take a temperature 
#print "<tempearture> is hot" if the temperature is >= 80
# otherwise, print "<temperature> is not hot"
#temperature = 81  #both work could ask or be integrated 
temperature = int(input("what is the temperature\n>"))
#if, boolean expression, :
# sort of like a function, no parenthessis
if temperature >= 80:
    print("the temperature is " + str(temperature) + " degrees.")
    print(str(temperature) + " degrees is hot")

else:   #else takes no condition adn runs when the if above is false 
    #otherwise.....
    print("the temperature is " + str(temperature) + " degrees.")
    print(str(temperature) + " degrees is not hot")



password = input("what is the password\n>")
if password == "skibidi68" :
    print("access granted")

else :
    print ("access denied")




question_1 = input("what's 5 + 5")
if question_1 == "10":
        print("right")
        tally_score = 1
else :
    print ("wrong")
    tally_score = 0

question_2 = input("whats my name")
if question_2 == "ryan" :
        print("right")
        tally_score = tally_score + 1
else :
    print ("wrong")
    tally_score= tally_score + 0


question_3 = input("what color is the sky")
if question_3 == "blue" :
        print("right")
        tally_score= tally_score +1
else :
    print ("wrong")
    tally_score= tally_score + 0

question_4 = input("what color is grass")
if question_4 == "green" :
    print("right")
    tally_score=tally_score + 1
else :
    print ("wrong")
    tally_score=tally_score+0


question_5 = input("what color is the sun")
if question_5 == "yellow" :
        print("right")
        tally_score=tally_score+1
else :
    print ("wrong")
    tally_score=tally_score+0


def tally_score1 ():
    print(tally_score + "/5")

tally_score1()