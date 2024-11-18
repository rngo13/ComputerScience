#there are a couple types of loops in python
#the for loop lets you iterate a list
#great for looping a set number of times
# but what if we need to loop an uncertain number of times??
# ex. entering your password
# you could get it rihg tthe firs titme 
# it could take you a million tries
#or anything in between


real_password = "potato"
enter_pass = ""


#a while loop continutes looping until the condition is no longer true 
while real_password != enter_pass:  #check if the entered password matches the real one
    #ask for the password
    enter_pass = input("Please enter the password\n")
    #check if password is correct
    if enter_pass == real_password:
        print("access granted")
    else:
        print("access denied")
        print("try again")
#end password checking
print("welcome!")


# try this
#update this while loop so that it prints how many attempts you are on
#print number of attempts every loop


real_password = "potato"
enter_pass = ""

attempts = 0

#a while loop continutes looping until the condition is no longer true 
while real_password != enter_pass:  #check if the entered password matches the real one
    #ask for the password
    enter_pass = input("Please enter the password\n")
    attempts = attempts + 1
    #check if password is correct
    if enter_pass == real_password:
        print("access granted")
    else:
        print("access denied")
        print("try again")
        print(str(attempts) + " atempts")
        
#end password checking
print("welcome!")



#with while loops, you need to be careful for infinite loops
#when you pt your computer in rest mode, it has nightmares /joke
#an infinite loops happens when you enter a while loop that can be escaped 
#example(do not click run)




count = 0
while count < 10:
    count += 1
    print (count)

print("all done")


#real world example
#type exit to quit

user_input = ""

while user_input != "exit":
    user_input = input("enter something (type 'exit' to quit)")
    print("you entered: " + user_input)

print("all done")