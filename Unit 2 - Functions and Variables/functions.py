def top_five_movies ():                   #Define a new function
    print("these are my top 5 movies!")
    print("spiderman into the spiderverse")
    print("whiplash")
    print("spongebob out of water")
    print("avengers")
    print("sonic")        #

def add (x,y):
    print (x + y)

add(4,2)
add(653244567543,86543567)





def top_five_movies(movie_1,movie_2,movie_3,movie_4,movie_5) :
    print("1. " + movie_1)
    print("2. " + movie_2)
    print("3. " + movie_3)
    print("4. " + movie_4)
    print("5. " + movie_5)

top_five_movies ("avengers","rangers","star","emoji","lego") #Need to be in parentheses to run
#need paramters which is the things inside parentheses

num_1 = int(input("whats the first number?\n>"))
num_2 = int(input("whats the second number?\n>"))

add(num_1,num_2)



x = 4
def my_function():
    global x    #From now on, when I call x, I'm talking about the global version!! Not the local verison...
    x = 5       #Reassigning the global variable x
    print(x)    #Prints 5

print(x)  
my_function()



def add(x,y) :
    print(x + y)
    #this is a function without a return
    #it is totally okay for function to not return anything

add (10,9)



def add(x,y) :
    return x + y

sum=add (10,9)
print(sum)







def calculate_tax(item_1,price_1,rate_1) :
    item_1 = input("what is your item")
    price_1 = float(input("whats is the price of your item"))
    rate_1 = float(input("what is the rate of your item"))
