# Lists in Python

"""
A list is a built-in data structure in Python used to store multiple itiems in a single variable
List are ordered, mutable, and allow allow duplicated valures.

variable_name = [item1, item2, item3,...]
"""

my_list = [10, 20,30, 40]
print(my_list)

mixed_list =[1, "apple", 3.5, True]
print(mixed_list)

#accessiing Items 
 #       [0]         [1]         [2]
fruits =["apple", "bananna", "cherry"]
print(fruits[0]) #first element
print(fruits[1]) #seccond item
print(fruits[2]) #third item
print([fruits[-1]]) #last item
print([fruits[-2]]) #second to last item 

#slicing lists
print(fruits[0:2]) #items from index 0 up to (but not including 2)
print(fruits[:2]) #first 2 elements 
print(fruits[1:]) #from index 1 to the end 

#modifing lists
fruits[1]="Mango"
print(fruits)

#adding items
fruits.append("orange") #adds to the end 
print(fruits)

fruits.insert(1,"kiwi") #inserts at index 1
print(fruits)

#removing items 
fruits.remove("apple") # remove by value
print(fruits)

fruits.pop() #remove last item
print(fruits)

del fruits[0] #removes item at index 0
print(fruits)

#list length
print(len(fruits))
print(len(["cohort63", True, "Python", 3.1416, 2025]))

"""
----------------------------
Min-Challenge: Favorite Movie
----------------------------

Create a list of 4 favorite movies
Replace the second movie (index 1) with a new one
Remove one movie
    Option A: Remove by Value
    Option B: Remove by index
    Print the list
    Print the length
"""
print("------Mini-Challenge 1------")
movies =["Neon Gensis", "I am legend", "Triangle","Boondock Saints"]
movies[1] = "Avatar"
del movies[0] # Remove by index
print(movies)
print(len(movies))

#-------assignment #2--------
