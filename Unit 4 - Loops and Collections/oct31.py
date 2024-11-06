# python has gour tpes of collections
#tuples
#set
#list
#dictionary

# today, were going to focus on listssssssssts

#a list is a way to store more than one value in a signle variable

#those values in the lists are called ITEMS
#ITEMS can be accessed by their index(position in the list)

#index                          0                   1               2               3               4
best_elden_ring_weapons = ["blasphemous blade","moonveil", "rivers of blood", "iron ball", "bloodhounds fang"]


#idex           0    1    2    3
best_years = [1776,1985,1993,1957]


print(best_years.index(1985))




#print the best elden ring weapon 
print(best_elden_ring_weapons[0])

#print the worst of the best elden ring weapom
print(best_elden_ring_weapons[len(best_elden_ring_weapons)-1])




#list items can be changed 
best_elden_ring_weapons[3] = "spiked fist"
print(best_elden_ring_weapons)



#remove the last item in the list
# the .pop() function removes an item in a list by its positon in the list
best_elden_ring_weapons.pop(4)
print(best_elden_ring_weapons)


#remove an item by its value
best_elden_ring_weapons.remove("moonveil")
print(best_elden_ring_weapons)


#add a new item to the end of a list 
best_elden_ring_weapons.append("Mohgwyns sacred spear")
print(best_elden_ring_weapons)


import random
numbers = [random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100)],
print(numbers)
print(max(numbers))
print(min(numbers))
numbers.sort()
print(numbers)


#strings are lists
#strings are just a list of characters 
word = "potato"
print(word[0])
print(word[len(word)-1])




import time
for i in range(0,17):
    time.sleep (.15)
    print("FAH")
    print(i)
