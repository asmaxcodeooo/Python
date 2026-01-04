#for loop - range

for i in range(5):
    print(i)

for i in range(1, 20):
    if i % 2 == 0:
        print(i)

#break

for i in range(1, 10):
    if i == 3:
        break
    print(i)

#continue

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

#for loop through list

fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)

#for loop through tuple

vegetables = ("Tomato", "Potato", "Brinjal")

for vegetable in vegetables:
    print(vegetable)

#for loop - dictonary

student = {"name": "Sanket", "age":21, "college": "SNJB COE"}

for item in student:
    print(item, student[item])

#for loop - string

text = 'python'
for i in text:
  print(i)

#print pattern with for loop

rows = int(input("Enter the rows  :"))
for i in range(0, rows+1):
    for j in range(i):  
        print("*", end='')
    print()