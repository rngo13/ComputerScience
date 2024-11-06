import random #import random

#generate a list of give random integers from 0-99
nums = [random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100), ]

#print the list before it is sorted
print(nums)


#define the function
def bubble_sort(numbers):#take the list as a parameter
    #create a varaible for how many steps we are taking, start at zero 
    steps=0

    #check if the list is sorted as many times as their are list items 
    for j in range(0,len(nums)-1):

        #iterate through every item in the list 
        for i in range(0,len(numbers) - 1):
            
            #check if the current list item is greater than the next list item
            if numbers[i] > numbers [i+1]:
                
                #swap their values
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                
                #increase number of steps
                steps +=1
   
    print(numbers)
    print("completed in " + str(steps) + " steps")



bubble_sort(nums)




import random
nums = [random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100), ]


print(nums)



def quick_sort(n):
    
    pivot = n[-1] #set pivot as the last number 

    #first number from the left that is larger
    lPos=0
    #first number from the right tht is smaller
    rPos = len(n)-1 #set to default

    for j in range(0,len(n)):
    #find l
        for i in range (0,len(n)):
            if n[i] > pivot:
                lPos = i 
                break

    #find r 
        for i in range(len(n)- 1, -1, 1):
            if n[i] < pivot:
                rPos = i 
                break


    #check if l index is greater than r index
        if lPos > rPos:
            n [lPos],n[-1] = n[-1], n [lPos]
            break
        else:
            n[lPos],n[rPos] = n[rPos], n[lPos]

    
    quick_sort()

    print(n)

quick_sort(nums)