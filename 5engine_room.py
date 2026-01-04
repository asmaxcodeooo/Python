fruits = ("Apple", "Banana", "Mango", "Orange", "Grapes")
print(fruits)
print(type(fruits))

#accessing elements of tuple

print(fruits[0]) #from start
print(fruits[-1]) #from end

print(len(fruits)) #length

print(fruits.index("Orange")) #check index

if "Mango" in fruits:
    print("Mango is in the tuple") #check element

for fruit in fruits:
    print(fruit)     #loop

vegetables = ("Tomato", "Potato","Brinjal")
print(vegetables)  #new tuple

inFridge = fruits + vegetables # concatenation pf tuples
print(inFridge)