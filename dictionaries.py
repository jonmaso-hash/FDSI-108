#dictionaries in Python

"""
A dictionary is a bult-in data structure in Python to sore data in key: value pairs.
Dictionaries are mutable, ordered, keys must be unique.

OPTION 1
my_variable = {"key1": value1, "key2:" value2, ...}

OPTION 2
my_variable = {
"key1": value1,
"key2": value2,
...
}
"""

#creating a dictionary
student ={
    "name": "John",
    "age": 68,
    "major": "Computer Sceince"
}

print(student)

new_student ={
    "name": "Pam",
    "age": 31,
    "name": "Angela" #if you use the same key twice, the last value will overwrite the previous.
}
print(new_student)

#accesing items
print(student["name"])
print(student["age"])
[print(student["major"])]

#adding new items
student["graduation_year"] = 2025
print(student)

#changing values
student["age"] = 20
print(student)

#Removing items
student.pop("major") # remove by key
print(student)

del student["name"] #remove specific key
print(student)

#dictinary length
print(len (student))

#clearing dictionaries
student.clear()
print(student)

#nested dictionaries
students_group ={
    "student_one":{
        "name": "bruce",
        "age": 20
    },
    "student_two":{
        "name":"Peter",
        "age":89
    }
}

print(students_group)
print(students_group["student_two"]["name"])

"""
----------------------------
Mini-Challenge: Song Metadata
-----------------------------

Create a dictionary called song with keys: "title:, "artist", "duration".
Print the "title" value.
Add a new key "album"
Upadte "duration" to a new value.
Remove "album"
Print the dictioanry lngth. 

add a print after every step
"""
song = {
    "title": "Beat it",
    "artist": "Michael Jackson",
    "duration": 3.38
}
print(song["title"])

song["album"] = "Bad"
print(song)


song["duration"] = 4
print(song)

song.pop("album")
print(song)


print(len(song))
