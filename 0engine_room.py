student = {"name": "asma","age": 21,"course": "Python",}
print(student)

print(student["name"])

student["grade"] = "B"
print(student) 

student["grade"] = "A"
print(student) 

print(student.keys()) 
print(student.values()) 

student.pop("grade")
print(student) 

print(len(student))

if "course" in student:
    print("Course is available") 

for key, value in student.items():
    print(key, ":", value)

#nested dict

students = {
    "student1": {
        "name": "Mariya",
        "age": 19,
        "course": "C++"
    },
    "student2": {
        "name": "Risa",
        "age": 21,
        "course": "Java"
    }
}
print(students)