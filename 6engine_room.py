#math
import math

a = 10
b = 5

# Addition
add = a + b
print("Addition:", add)

# Subtraction
sub = a - b
print("Subtraction:", sub)

# Multiplication
multiply = a * b
print("Multiplication:", multiply)

# Division
div = a / b
print("Division:", div)

# Square root
sqroot = math.sqrt(25)
print("Square root of 25:", sqroot)

# Cube
cube = math.pow(3, 3)
print("Cube of 3:", cube)

# Value of pi
pi = math.pi
print("Value of pi:", pi)


#datetime
import datetime

#date & time both
now = datetime.datetime.now()
print(now)

#date only
today = datetime.date.today()
print(today)

#time only
current_time = datetime.datetime.now().time()
print(current_time)

#format change
now = datetime.datetime.now()
print(now.strftime("%d-%m-%Y %H:%M:%S"))




print("Array a:", a)
print("Array b:", b)

# Basic operations
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)