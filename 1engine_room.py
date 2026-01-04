subscribed = True;
if subscribed:
    print('Thank you for subscribing!')
else:
    print('Not subscribed, please subscribe.')



numbers=[10,80,20,60,30,40,50] 
print(numbers) 
numbers.sort()
print(numbers) 
numbers.reverse()
print(numbers)



courses = ['ba', 'bcom', 'bsc', 'be', 'ma', 'mcom',' msc', 'me']
print(len(courses)) 
for x in courses:
    print(x) 



a=[10,40,[58,67,89,[45,25]],43,60]
print(a)
print(a[1])
print(a[2][3][0])
print(a[2]) 



courses = ('ba', 'bcom', 'bsc', 'be', 'ma', 'mcom',' msc', 'me')
print(courses[3:5])  
print(courses[3:])   
print(courses[:3])
print(courses[3]) 
print(courses[-1]) 



string="How are you?"
print(string[-1])
print(string[4])
print(string[1:6])
print(string[:-1])



company = {
    'name': 'Apple',
    'year': 1975,
    'founders': {
        'first': 'Steve Jobs',
        'second': 'Steve Wozniak'
    }
    }
print(company) 



def calculator(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
    print(a**b)
    print(a//b)

calculator(2,4)




n = int(input(" Enter a number to check:"))

if n % 2 == 0:
  print("It's an even number.")
if n % 2 != 0:
  print("It's an odd number.")
if n == 0:
  print("The number is neither even nor odd. Rather you entered Zero.")




def calc(a,b):
   c=int(input('Enter yoour choice:'))
   if c==1:
      d=a+b
      print(d)
      
   elif c==2:
      d=a-b 
      print(d)

   elif c==2:
      d=a*b  
      print(d)

   elif c==2:
      d=a/b 
      print(d) 

   else:
      print("Enter a valid choice!")


calc(2,4)




rows = int(input("Enter the rows  :"))    
for i in range(0, rows+1):              
    for j in range(i):                
        print("*", end='')             
    print()

rows = int(input("Enter the rows  :"))    
for i in range(0, rows+1):              
    for j in range(i):                
        print("  ", end='*#')               
    print()




x = 1
while x < 10:
    if x == 6:
        break
    print(x)
    x += 1





class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    
    def details(self):
        print("Employee Name: ",  self.name)
        print("Employee Age: ", self.age)
 

emp1 = Employee("John", 26)        
emp2 = Employee("Jane", 24)         

emp1.details()
emp2.details()






import math
print(math.sqrt(16))
print(math.sin(45))
print(math.log10(100)) 
print(math.gcd(16,24)) 
print(math.lcm(16,24)) 

from datetime import date
today=date.today() 
print(today) 
print(today.day,today.month,today.year)

from datetime import datetime
print(datetime.now())