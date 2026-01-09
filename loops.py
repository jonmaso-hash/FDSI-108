"""
Loops

A for loop in Python is a control structure that lets you repeat a block of code foreach item in sequence 
such as (list, string, tuple, dictionary, or a range of numbers )

for variable in sequence: 
    - Code block runs for reach item in the sequence
"""

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit) 

print ("-----------1-------------->")

for letter in "John": 
    print(letter)

print ("------------2------------->")

for number in range(5):
        print(number) # prints 0,1,2,3,4 range() only includes numbers less than the stop value

for number in range (2, 6):
    print(number)

print ("-----------3-------------->")

for number in range(0, 10, 2):
        print(number)

"""
Mini challenge

1. Ask the user to enter a number and store it in a variable called num 
2. Use for loop with range (1,11) to repeat 10 times from (1 to 10)
3. Inside the loop, multiply num by the current loop value
"""

num = int(input("Enter a number: "))

for number in range(1,11):
    print(f"{num} * {number} = {num * number}")

print ("-----------4-------------->")

"""
While loops 

A while loops repeats a block of code as long as a condition is True
while condition: 
    -Code block runs as longn as condition is True
"""
print ("-----------5-------------->")
count = 1

while count <=5:
    print("Count is: ", count)
    count += 1

print ("-----------6-------------->")

number = 0

while True: #infinite loop 
    print(number)
    number += 1
    if number ==8:
        break #stop the loop when number reaches 8