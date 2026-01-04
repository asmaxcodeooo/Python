var="Hello Asma!"
print(var[2:7])
print(var[:5])
print(var[4:])

num1=10
num2=15
print(num1-num2)
print(num1*num2)
print(num2 / num1)  
print(num2 // num1) 
print(num2 % num1) 


fir = 40
sec = 0.1
print (fir + sec)

text = input('Enter some text    ->')    
print(text.upper())
print(text.title())
print(text.find('a'))
print(text.count('h'))
print(text.replace('a','h'))
print(len(text))


print(abs(-4))
print(abs(-4.5))

a=4
b=5
if 4 > 5:
    print('four is greater than five')
else:
    print('four is smaller than five')

is_subscribed = True
if is_subscribed:
    print('Thank you for the subscription!')
else:
    print('Please subscribe')


colors = ['bule', 'maron', 'orange', 'red', 'pink', 'black']
print(colors) 
print(type(colors))
c = 'brown'
colors.append(c)   
print(colors) 
colors.sort
print(colors)
print(colors.reverse)
print(len(colors))
for item in colors:
    print(item)


fruits=('orange','banana','apple')
print(fruits)
print(type(fruits))
print(fruits.index('orange'))
print(fruits.count('orange'))
for id, item in enumerate(fruits):   
  print(id, item)
print('apple' in fruits)


new = tuple(colors)
print(colors)
print(new)

# Dictionary
details= {
    "name": "Asma Shamashuddin Mujawar","class":"M.Sc(IMCA)",
    "skills": "Python"
}
print(details)
print(details['name'])
del details['skills']
print(details)

company = {
    'name': 'Apple', 'year': 1975,
    'founders': {'first': 'Steve Jobs','second': 'Steve Wozniak'}
    }
print(company)

# Function
def hello (name):
  print(f'hello {name}') 
hello('John')
hello(12)
print(type(hello))

p = int(input("Enter the principle amount? "))    
r = float(input("Enter the rate of interest? "))     
t = int(input("Enter the time in years? "))
def simple_interest(p,t,r):    
    return (p*t*r)/100      
print("Simple Interest: ",simple_interest(p,r,t))   

# If
n = int(input(" Enter a number to check:"))
if n % 2 == 0:
  print("It's an even number.")
if n % 2 != 0:
  print("It's an odd number.")
if n == 0:
  print("The number is neither even nor odd. Rather you entered Zero.")

#If Elif
marks = int(input("Enter the marks? "))  
if marks > 85 and marks <= 100:  
   print("Congrats ! you scored grade A ...")  
elif marks > 60 and marks <= 85:  
   print("You scored grade B + ...")  
elif marks > 40 and marks <= 60:  
   print("You scored grade B ...")  
elif (marks > 30 and marks <= 40):  
   print("You scored grade C ...")  
else:  
   print("Sorry you are fail !!")  

# Nested If
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

# break statement
for item in colors:
   print (item)
   if item == 'red':
      break
for item in colors:
   print (item)
   if item == 'red':
      continue
   print(colors)

# While loop
class Employee:            
    name = "asma"          
    age = 2
    def hello(self):     
      print("Hello")
emp = Employee()           
emp.hello()   

class Dog:
  def _init_(self, breed, age, color):
    self.breed = breed
    self.age = age
    self.color = color
  def details(self):
    print(f"Breed - {self.breed}, Age - {self.age}, Color - {self.age} ")
dog1 = Dog('Husky', 5, 'Blank')
dog1.details()

#Maths Module
import math
math.sqrt(4)  
math.log10(100)
math.sqrt(60)
math.pi
print(math.sin(math.radians(90)))