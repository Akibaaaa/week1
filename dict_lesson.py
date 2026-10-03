students = {}

name = input("enter the student name: ")
age = int (input("enter the student age: "))
dept = input("enter the student dept: ")
gpa = float(input("enter the student gpa"))
students= {
    "name" : name,
    "age":  age,
    "dept" : dept,
    "gpa" :gpa}
student = {
    "name": "Abebe",
    "age": 20,
    "department": "Software Engineering",
    "gpa": 3.5
}
print(student)
print(student["name"])
print(student["age"])
student["Gpa"] = 3.7
student["year"] = 3
print(student)



students = {}
num = int(input("how many students: "))
for i in range(num):
    name = input(":")
    age = int(input("age:"))
    gpa = float(input("Gpa:"))
    students[name]= {
        "age" : age,
        "gpa" : gpa
    }
print(students)

grades = {
    "Abebe": 85,
    "Selam": 92,
    "Dawit": 45,
    "Hana": 78,
    "Kebede": 50,
    "Sara": 35
}
for key, values in grades.items():
    print(key, values)
high = 0
for values in grades.values():
    if values > high:
        high = values
print(high)
low = 100
for values in grades.values():
    if values < low:
        low = values
print(low)
score = []
for i in grades.values():
    score.append(i)
    avg = sum(score)/len(score)
print(avg)
count_above = 0
count_below = 0
for values in grades.values():
    if values >= 50:
        count_above += 1
    else:
        count_below += 1
print(count_above, count_below) 


inventory = {
    "bread": 20,
    "milk": 15,
    "rice": 30,
    "pasta": 10,
    "eggs": 50
}
for key, values in inventory.items():
    print(key, values)
search = input("enter what u want: ")
for key, values in inventory.items():
    if key == search:
        print(key, values)

searchh = input("what item do u want to change the quantity: ")
if searchh in inventory:
    quuan = input('entree the new quantity:')
    inventory[searchh] = quuan

removalof = input("what do u want to remove")
result = inventory.pop(removalof)
print(result)
for key, values in inventory.items():
    if values < 15:
        print(key)


search = input("input the name:")
for search in inventory:
    print(search, inventory[search])




students = {
    "Abebe": {
        "age": 20,
        "department": "Software Engineering",
        "gpa": 3.5,
        "year": 3
    },

    "Selam": {
        "age": 21,
        "department": "Computer Science",
        "gpa": 3.8,
        "year": 4
    }
}
for name, infn in students.items():
    print(name, infn)
for name, infn in students.items():
    print(name, infn["age"])





 