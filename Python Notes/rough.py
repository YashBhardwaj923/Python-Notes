
#! Python Lambda Function:-

#* A lambda function is a small anonymous function.
#* A lambda function can take any number of arguments, but can only have one expression. 
#* Syntax:- lambda arguments : expression

# examples:
# 1.
sum = lambda a, b : print(a + b)
sum(4, 5)
'''
    sum --> variable name
    lambda --> keywords
    a, b --> parameters
    : --> colon for block
    print(a + b) --> expression
    sum(4, 5) --> function call with arguments
'''

# 2.
sayHi = lambda name : print("Hello " + name)
sayHi("Gopal Bhardwaj")

# 3. with return function:
info = lambda name, age, city : f"My name is {name}. I am {age} years old. I am living in {city}."
print(info("Gopal Bhardwaj", 28, "San Francisco"))

# 4. parameters with input:
""" name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")

info = lambda name, age, city : f"My name is {name}. I am {age} years old. I am living in {city}."
print(info(name, age, city)) """

#* return function in a function:
def main():
    return lambda a, b : a * b

out = main()
print(out(2, 3))
