import time
import random


score = 0
opp_score = 0


def one_v_one():


    global opp_username
    global username_random
    username_random = ["newblancher678", "Megagamer678", "Hugecow345", "supernewb345", "jaymakethat_money", "8wayjohnathon1", "Xx_incredible_tv_xX", "d1i1d1d1y"]
    opp_username = random.choice(username_random)
    print("\nMatchmaking... (Ranked Duel - Diamond 1 Division 4)\n")
    time.sleep(2.5)
    print("Match Found\n")
    time.sleep(1)
    print("Entering match in 3...")
    time.sleep(1)
    print("Entering match in 2...")
    time.sleep(1)
    print("Entering match in 1...")
    time.sleep(1)
    print("Match Entered.\n")
    time.sleep(.5)
    print("You are playing against " + str(opp_username) + ", first player to 3 goals wins!\n")
    kickoff()


def kickoff():
    global score
    global opp_score
    time.sleep(1.6)
    print("Kickoff in 3...\n")
    time.sleep(1)
    print("Kickoff in 2...\n")
    time.sleep(1)
    print("Kickoff in 1...\n")
    kickoff_selection = input("What kickoff are you gonna use?\n\nA) Speed Flip Kickoff\nB) Delayed Kickoff\nC) Fake Kickoff\n>").lower()
    if kickoff_selection == "a":
        kickoff_outcome_1()
    elif kickoff_selection == "b":
        kickoff_outcome_2()
    elif kickoff_selection == "c":
        kickoff_outcome_3()
    else:
        print("Invalid input, try again.")
        kickoff()


def kickoff_outcome_1():
    win_chance = random.random()
    if win_chance <= .25:
        global score
        global opp_score
        score = (score + 1)
        print("\nYou won the kickoff And scored, the score is now " + str(score) + " - " + str(opp_score) + "\n")
    elif win_chance  > .25 and win_chance <= .75:
        print("\nYou won the kickoff and the ball is on " + str(opp_username) + "'s side!\n")
        choose_to_shoot()
    else:
        opp_score = (opp_score + 1)
        print("\nYou lost the kickoff and " + str(opp_username) + " scored, the score is now " + str(score) + " - " + str(opp_score) + "\n")


def kickoff_outcome_2():
    win_chance = random.random()
    if win_chance <= .7:
        select_after_kickoff()
    elif win_chance > .7:
        print("\nYou lost the kickoff, the ball is going towards your goal.\n")
        defend()


def kickoff_outcome_3():
    global score
    global opp_username
    global opp_score
    win_chance = random.random()
    if win_chance <= .80:
        print("\n" + str(opp_username) + " hit the ball towards you\n")
        choose_to_shoot()
    elif win_chance > .80 or win_chance <= .95:
        print("\n" + str(opp_username) + " realized you faked, and is now dribbling towards your goal.\n")
        defend()
    elif win_chance > .95:
        opp_score = (opp_score + 1)
        print("\nYou didn't manage to defend when you faked the kickoff\n")
        print("\n" + str(opp_username) + " scored on you, the score is now " + str(score) + " - " + str(opp_score) + "\n")


def choose_to_shoot():
    choice = input("\nWould you like to...\n\nA) Shoot the ball\nB) Play defensive and go back to your goal post\n>").lower()
    if choice == "a":
        shooting_ball()
    elif choice == "b":
        defend()
    else:
        print("\nInvalid input, try again.\n")
        choose_to_shoot()


def go_to_goal():
    global score
    global opp_score
    win_chance = random.random()
    if win_chance <= .5:
        print("\nYou made it back to the goal!\n")
        defend()
    else:
        score = (score + 1)
        print("\nYou didnt make it back in time. The score is now " +str(score) + " - " + str(opp_score) + "\n")


def press_f():
    F = input("\nPress F to go to go to your goal and defend!\n>").lower()
    if F == "f":
            go_to_goal()
    else:
        print("\nInvalid input, try again.\n")
        press_f()


def rush_ball():
    global opp_username
    win_chance = random.random()
    if win_chance <= .3:
        print("\nYou didn't make it to the ball fast enough\n")
        press_f()
    elif win_chance > .3:
        print("\nYou made it to the ball before " + str(opp_username) + "\n")
        shooting_ball()


def won_boost_over_ball():
    selection = input("\nYou got the boost, would you like to...\n\nA) Shoot the ball\nB) Dribble the ball\n>").lower()
    if selection == "a":
        shooting_ball()
    elif selection == "b":
        dribble_ball()


def boost_over_ball():
    global opp_username
    win_chance = random.random()
    if win_chance <= .3:
        won_boost_over_ball()
    elif win_chance > .3:
        print("\nYou took too long getting boost, " + str(opp_username) + " hit the ball towards your goal, defend!\n")
        defend()


def demolish():
    global opp_username
    win_chance = random.random()
    if win_chance <= .45:
        print("\nYou demolished " + str(opp_username) + "\n")
        choose_to_shoot()
    elif win_chance > .45 or win_chance <= .85:
        print("\nYou didn't manage to demolish " + str(opp_username) + ", and your opponent is now going towards your goal, defend!\n")
        defend()
    else:
        print("You bumped " + opp_username + ", shoot!\n")
        shooting_ball()


def select_after_kickoff():
    selection = input("\nYou won the kickoff, would you like to...\n\nA) Rush the ball without boost. \nB) Go to boost instead of the ball. \nC) Try to demolish " + opp_username + ".\n>").lower()
    if selection == "a":
        rush_ball()
    elif selection == "b":
        boost_over_ball()
    elif selection == "c":
        demolish()
    else:
        print("\nInvalid input, try again.\n")


def musty_flick():
    global score
    global opp_score
    win_chance = random.random()
    if win_chance <= .75:
        score = (score + 1)
        print("\nYou scored the musty flick! the score is now " + str(score) + " - " + str(opp_score) + "\n")
    elif win_chance > .75:
        print("\nYou hit the crossbar!\n")
        crossbar_decision()


def breezy_flick():
    global score
    global opp_score
    win_chance = random.random()
    if win_chance <= .4:
        score = (score + 1)
        print("\nYou scored the breezy flick! the score is now " + str(score) + " - " + str(opp_score) + "\n")
    elif win_chance > .4:
        print("\nYou did the breezy flick , but you hit the crossbar\n")
        crossbar_decision()


def flick_selection():
    selection = input("\nWould you like to...\n\nA) Musty flick\nB) Breezy flick\n>").lower()
    if selection == "a":
        musty_flick()
    elif selection == "b":
        breezy_flick()
    elif selection != "a" or selection != "b":
        print("\nInvalid input, try again.\n")
        flick_selection()


def dribble_ball():
    global score
    global opp_score
    global opp_username
    win_chance = random.random()
    if win_chance <= .9:
        print("\nYou are dribbling towards Megagamer678's goal!\n")
        flick_selection()
    elif win_chance > .9:
        opp_score = (opp_score + 1)
        print("\n" + str(opp_username) + " got to the ball and scored before you could dribble, the score is now " + str(score) + " - " + str(opp_score) + "\n")


def choose_offense():
    choice = input("\nDo you want to...\n\nA) Shoot the ball\nB) Dribble the ball to the goal\n>").lower()
    if choice == "a":
        shooting_ball()
    elif choice == "b":
        dribble_ball()
    elif choice != "a" or choice != "b":
        print("\nInvalid input, try again\n")
        choose_offense()


def defend():
    global score
    global opp_username
    global opp_score
    button_press = input("\nPress X to defend.\n>").lower()
    if button_press == "x":
        win_chance = random.random()
        if win_chance <= .50:
            score = (score + 1)
            print("\nYou saved the ball and scored on " + str(opp_username) + "'s goal! The score is now " + str(score) + " - " + str(opp_score) + "\n")
        else:
            opp_score = (opp_score + 1)
            print("\nYou failed to defend. " + str(opp_username) + " scored on you and the score is now " + str(score) + " - " + str(opp_score) + "\n")
    elif button_press != "x":
        print("\nInvalid input, try again\n")
        defend()


def defending_shot():
    global opp_username
    global score
    global opp_score
    button_press = input("\nPress X to defend.\n>").lower()
    if button_press == "x":
        win_chance = random.random()
        if win_chance <= .50:
            print("\nYou saved the ball!\n")
            shooting_ball()
        else:
            opp_score = (opp_score + 1)
            print("\nYou failed to defend. " + str(opp_username) + " scored on you and the score is now ." + str(score) + " - " + str(opp_score) + "\n")
    elif button_press != "x":
        print("\nInvalid input, try again\n")
        defending_shot()


def shooting_ball():
    global score
    global opp_score
    input("\nPress X to shoot the ball!\n>")
    score_chance = random.random()
    if score_chance <= .7:
        score = (score + 1)
        print("\nYou scored! The score is now " + str(score) + " - " + str(opp_score) + "\n")
    else:
        print("\nYou missed the shot.\n")
        defend()


def press_x():
    x = input("\nYou missed the double touch. Press X to go back to your goal and defend!\n>").lower()
    if x == "x":
        defend()
    else:
        print("\nInvalid input, try again.\n")
        press_x()


def double_touch():
    global score
    global opp_score
    win_chance  = random.random()
    if win_chance <= .6:
        score = (score + 1)
        print("\nYou scored the double touch! The score is now " + str(score) + " - " + str(opp_score) + "\n")
    else:
        press_x()


def crossbar_decision():
    choice = input("\nWould you like to\n\nA) Jump for the double touch\nB) Back off and defend.\n>").lower()
    if choice == "a":
        double_touch()
    elif choice == "b":
        defend()


def rush_ball():
    global score
    global opp_score
    global opp_username
    win_chance = random.random()
    if win_chance <= .8:
        print("\nYou got to the ball first!\n")
        win_chance = random.random()
        if win_chance <= .85:
            score = (score + 1)
            print(username + " scored! The score is now " + str(score) + " - " + str(opp_score) + "\n")
        else:
            print("\nYou hit the ball off of the crossbar.\n")
            crossbar_decision()
    elif win_chance > .8:
        print("\n" + str(opp_username) + " got to the ball first, go defend!\n")
        defend()


def offensive_kickoff():
    global opp_username
    selection = input("\nWould you like to...\n\nA) Rush the ball without boost. \nB) Go to boost instead of the ball. \nC) Try to demolish Megagamer768.\n>").lower()
    if selection == "a":
        rush_ball()
    elif selection == "b":
        print("\n" + str(opp_username) + " got to the ball before you, the ball is now on your side. Defend.\n")
        defend()


def game_welcome():
    print("\nWelcome To Rocket League!")
    global gamemode_selection
    gamemode_selection = input("\nWould You Like To Play 1v1?\nA) Play 1v1\nB) Dont play Rocket League\n>").lower()
    if gamemode_selection == "a":
        one_v_one()
    elif gamemode_selection == "b":
        print("You have no choice, press a")
        game_welcome()
    elif gamemode_selection != "a" or gamemode_selection != "b":
        print("\nInvalid choice, try again.\n")
        game_welcome()


def left_match():
    print("\n\nGood game! rate my game good plz i tried really hard")


def quick_chats():
    choice = input("\nPost game quick chats:\n\nA) Well Played.\nB) GG.\nC) That was fun!\nD) Proceed without chatting\n>").lower()
    if choice == "a":
        print("\n" + username + ": Well played\n")
        time.sleep(1.5)
        print(opp_username + ": GG.\n")
        time.sleep(1.5)
        input("\nPress any button to leave the match.\n")
        left_match()
    elif choice == "b":
        print("\n" + username + ": GG.\n")
        time.sleep(2.5)
        print(opp_username + ": This is Rocket League!\n")
        time.sleep(1)
        input("\nPress any button to leave the match.\n")
        left_match()
    elif choice == "c":
        print("\n" + username + ": That was fun!\n")
        time.sleep(3)
        print("Server: " +  opp_username + " left the match.\n")
        time.sleep(1)
        input("\nPress any button to leave the match.\n")
        left_match()
    elif choice == "d":
        left_match()
    elif choice != "a" or choice != "b" or choice != "c" or choice != "d":
        print("\nInvalid input, try again.\n")
        quick_chats()


def game_results():
    global score
    global opp_score
    global opp_username
    score = int(score)
    if score == 3:
        print("You won " + str(score) + " - " + str(opp_score) + " against " + str(opp_username) + "!")
        time.sleep(2)
        quick_chats()
    elif score != 3:
        print("Unfortunately, you have lost " + str(score) + " - " + str(opp_score) + " against " + str(opp_username) + ".")
        time.sleep(2)
        quick_chats()


username = input("What is your username?\n>")
time.sleep(1)


def button():
    any = input("\nPress any button to continue.\n")
    if any == "":
        print("Please press a button, then enter.")
        button()
    else:
        game_welcome()


button()




def check_game_over():
    global score
    global opp_score
    if score < 3 and opp_score < 3:
        kickoff()
        check_game_over()
    else:
        game_results()


check_game_over()

