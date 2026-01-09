"""
Sets in Python 

A set is a built-in structure in Python to store unique items.
sets are unordered, unindexed and do not allow duplicate values.

my_set = {item1, item2, item3, ...}
"""
fruits = {"apple," "banana", "cherry"}
print (fruits)

fruits = {"apple," "banana", "apple"}
print(fruits) #duplicate "apple" is ignored

print("banana" in fruits)

fruits.add("orange")
print(fruits)

fruits.update(["kiwi", "mango"]) #add multiple items
print(fruits)

fruits.remove("kiwi") #removes item (error if not found)
print(fruits)

fruits.discard("watermelon") # removes item safely (no error if not found)
print (fruits)

#set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.union(set2)) #combine both with no duplicates
print(set1.intersection(set2)) #common element 
print(set1.difference(set2)) #elements in set1 but not in set2

#length
print(len(set1))

#copying sets
new_set = set1.copy()
print(new_set)

#clearing sets
set1.clear()
print(set1)