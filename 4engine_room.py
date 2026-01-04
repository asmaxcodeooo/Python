def hello():
    print('Hello Asma')

hello() #to print hello world

def greet_user(name):
    print("Hello", name)

greet_user("Asma")  #greet user

#for addtion
def add(a, b):
    return a + b

result = add(8, 4)
print("Addition of two numbers is ",result)

#similarly for substraction
def substract(a, b):
    return a - b

result = substract(8, 4)
print("Substraction of two numbers is ",result)

#for multiplication
def multiply(a, b):
    return a * b

result = multiply(8, 4)
print("Multplication of two numbers is ",result)

#for division
def divide(a, b):
    return a / b

result = divide(8, 4)
print("Division of two numbers is ",result)

#even or odd

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")