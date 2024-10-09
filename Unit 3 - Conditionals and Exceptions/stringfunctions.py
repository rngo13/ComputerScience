#string functions
# a group of like-functions that manipulate strings
# they modify strings
# SUPER easy and convenient to use
# Python would really not be fun wihtout them 

#  .lower()
# converts a string to all lowercase
# no matter what the input casing is, it si converted to lowercase 
# and the answer is lowercase
input_answer = "Lord of the Rings"
input_answer = input_answer.lower()#converts to "lord of the rings"
real_answer = "lord of the rings"
print(input_answer==real_answer)


# .uppwe()
# converts a strong to uppercase
x= "hello world".upper()
print(x)

# .capitalize()
# converts to lowercase, then capitalize the first letter
y = "HeLiO wOrLd".capitalize()
print(y) # Print "Hello World"


# .title()
# converts a string to titlecase
#capital first letters of words
z = "HeLiO wOrLd".title()
print(z)  #print "Hello World"


# .swapcase()
# It inverts the casing of each character
q = "Hello World!".swapcase()
print(q)    #prints "hELLO wORLD!"