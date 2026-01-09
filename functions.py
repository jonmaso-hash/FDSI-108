"""
Functions

A function is a block of code that only runs when it's called.
We can pass data to function(parameters). and tehy can return data as a result

def function_name(parameters):
    - code block(indented)
    -return value #optional
"""

def my_function():
    print("this is a funciton") # this line runs when the function is called

    #calling of the function
    my_function()

    def other_function():
        print("This is another function")

    other_function()

    def hello():
        cohort = 63
        print("Hello Cohort63", cohort)

        hello()
        hello()
        hello()
        my_function

    def get_full_name(first_name, last_name):
        return f"Hello {first_name} {last_name}" #sends back teh full name as text

   full_name = get_full_name("John", "Mason")
   print(full_name)

    #default parameter
   def greet(name="student"):
    print(f"Hello,{name}, welcome to class")
    greet()
    greet("Pam")