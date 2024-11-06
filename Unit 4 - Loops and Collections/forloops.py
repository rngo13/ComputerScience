#For loops 
#This is a big deal
#for loops allow the programmer to repeat, or what we call LOOP

#write a program that prints the numbers one through ten

#for <temp var om <lists>

#range(0,10) = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(0,10): #0 is the start value, 10 is the stop value 
    print(i)


top_foods = ["eggs benedict", "fried chicken", "mac n cheese"]
# go through every food in top foods
#repeats everything in the for loop for each item in the list
#where food equals the current item
for food in top_foods:
    print(food)



#practice:create a list of groceries -
#contains milk eggs bread butter apples
#ask for user input on an item they purcahsed
#if the item was on the list, print(item cross off the list )
#remove that item from the list
#you will need to use a for loop to search for that item
#you will need an if statement in the for loop to check


groceries = ["milk", "eggs", "bread", "butter", "apples"]

purchased_item = input("what item did you buy")

for grocery in groceries:
    if grocery == purchased_item.lower():
        print(grocery + " checked off the list!")
        groceries.remove(grocery)


print(groceries)




# create a list of five random numbers from 0-100
#use a for loop to find the sum of those numbers
import random
numbers = [random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100)]

for i in numbers:
  (i)