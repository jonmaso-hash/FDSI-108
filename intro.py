#Python Basics - sessions#1

print("Hello World from Python") #No semicolon needed at the end of lines
print(2) #Printing a number
print (5 + 3) #Printing the result of a math operation
print("Cohort#p63 Welcome")

#shortcuts
#Windows: Ctrl +s


#---- variable and concantations----

name = "Ruben"
age = 28
print(name) #Prints the variable value

print("My name is "+name+" and I am "+str (age))

first_name = "Michael"
middle_name = "John"
last_name = " Scott"
age = 46
print("My name is "+ first_name + " "+ middle_name +" " + last_name + " and I am "+str (age) + " year old.")

#--------F-String (cleaner way to format string)---------
print("hello")
print(f"My name is {first_name} {middle_name} {last_name} and I am {age} years old")

#multi-line f-string
print(f"""
My name is {first_name} {middle_name}{last_name}
and I am {age} years old. 
""")

#Minichallenge 1
"""
- Create 4 variables: my_name my_last_name, my_age, and my_favorite_technology.
- Assign them your own information or mock data.
- Then, use a f-string to print a sentence like the following: 
"Hello my name is _ _, I am _ years old and my favorite technology is_."


- Personalize the values with yur real data or fun mock data. 
You can also add extra variable (like city or hobby) to make  the sentence more creatative. 
"""
my_name = "john"
my_last_name = "mason"
my_age = 32
tech  = "javascript"
print(f"Hello my name is {my_name} {my_last_name}, I am {my_age} and my favorite tech is {tech}")


#type functions 
print(type("Peter"))
print(type(last_name))
print(type(True))
print(type(1234))

#--------Input Function---------
user_name = input("Enter your name: ")
print(f"Hello {user_name}")

user_age = int (input("Enter your age: "))
print(f"You are {user_age-1} years old.")
