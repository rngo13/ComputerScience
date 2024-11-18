#dictionary is a type of collection like list
#a list is a collection of items in a sequence
#a dictionary is different
#dictionaries store data in key-value pairs
# you can retreieve data quickly by using a unqiue key
# instead of retrieving it by index (position)

#example

#lists use brackets, dictionaries you braces
ryan = {
    "name":"ryan",
    "age": 17,
    "city": "albertville",
    "pets": 1,
    "height": 5.7
}

#each key must be unique 

# retrieiving values from a dictionary

print(ryan["age"])
#. get allows you to retrieve a value without erooring
# when the key doesnt exist
#the second parameter is what is given if value is not found
print(ryan.get("height"))
print(ryan.get("weight", "parleysss"))

#you can add values to a dictionary

ryan["country"] = "usa"

#you can modify values
ryan["age"] = 18

print(ryan)

#remove entries
ryan.pop("pets")

#iterate througha dictionary using a for loop

for key, value in ryan.items():
    print(key + ": " + str(value))

#dictionary functions

print(ryan.keys())      #returns all keys
print(ryan.values())    #returns all values
print(ryan.items())     #returns all pairs
print(ryan.keys())      #removes all items from the dict 



grades = {
    "alice":"A",
    "Bob":"B",
    "Charlie":"C",
    "David":"A",
    "Eve":"B",
}

student = {
    "name": "alice",
    "age": 16,
    "grade": "A"
}

print(student.get("name"))
print(student.get("age"))


student["grade"] = "A+"
print(student)



fav_movies = {
    "okay":2007,
    "hm":2008,
    "par":2009,
}

fav_movies["whiplash"] = 2043

print(fav_movies)


fruit_prices = {
    "apple":24,
    "orange":14,
    "pear":52,
    "grape":72,
    "lemon":8
}

fruit_prices.pop("apple")
print(fruit_prices)


inventory = {
    "apples":10,
    
}