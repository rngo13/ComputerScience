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