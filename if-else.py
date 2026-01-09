"""
if-else statement

an if-else statement in Python is a conditional control structure that lets you decide which 
block of code to run depending on whether a condition is True or False. 

The if block runs only if the condition evaulates to True. 
If the condition is False, the else block run instead. 
You can also add elif (else if) blocks to check multiple conditions in sequence. 

if conditions: 
- Code block runs if condition is True
elif another_condition: 
else: 
    - Code block runs if noe of the above condions are True 
"""
x = -7
x =10
x=90

if x > 0:
    print("x is postive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")

#nested if statements
if x > 0:
    if x < 20:
        print("x is a postive number less than 20")

# combining conditions
age = 18

if age >= 18 and age <= 21:
    print ("You are between 18 and 21 years old")

username = "john123"

if username == "peter57":
    print ("you are peter")

"""
Mini-challege 

1. Ask the user to enter a number from 0-100 and store in a variable called "score"
2. if the score is under 90 or above, print "Grade: A"
3. if the the score is between 80-89, print "Grade B"
4. if the score is between 70-79, print "Grade C"
5. Othewise, print "Grade F" 
"""

user_score =  int (input("Enter Your Score (0 -100): "))
if user_score <= 90: 
    print(f"score: {user_score} : A")

if user_score >= 80 and user_score<= 89:
    print (f"score: {user_score} : B")

if user_score>=70 and user_score<= 79: 
    print (f"score: {user_score} : C")
 
else: 
    print ("Your grade is a F")

score = int(input("Enter your score 0-100"))

if score <=90:
    print ("Grade A")
elif score >= 80: 
    print ("Grade: B ")
elif score >= 70:
    print ("Grade: C")
else:
    print("Grade: F")

"""
Mini-Challenge 

1. Ask the user to enter today's temprature in fahrenheit and store it in a variable called temperature 
2. use if-elif-else statements to classify the temperature: 
    if temperature >= 86, print "it's hot outside"
    if temperature >= 68, and temperature < 86, print "the weather is nice" 
    if temperature is >=50 and temperature < 68, print "It's a bit chilly"
    Otherwise, print "Its cold!"
"""

temperature = int(input("Enter the Temperature: "))


if temperature  >=86:
    print("Its hot outside")
elif temperature >= 68 and temperature< 85: 
    print("the weather is nice")
elif temperature >= 50 and temperature < 68: 
    print ("Its a bit chilly")
else: 
    print("its Cold!")