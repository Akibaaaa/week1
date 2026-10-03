x = (5)
print(type(x))


person =("rediet", 20, "AASTU")
name, age, uni = person
print(name)

name = "rediet"
age = "beki"
name, age = age, name
print(name)
print(age)


num = 5
students = []
'''for i in range (num):
    student = input("Enter the name of the student: ")
    students.append(student)'''
student_tuples =tuple(input("Input five names only").split())
if len(student_tuples) == 5
print(student_tuples)
first, *middle1, last = student_tuples
print(first)
print(last)
print(len(student_tuples))
print("Abebe" in student_tuples)



numbers = tuple(map(int, input("enter 8 numbers: ").split()))
print(numbers[0:3])
print(numbers[-3:])
print(numbers[2:6])
print(numbers[::2])
print(numbers[::-1])

student = ("Abebe", 21, "Software Engineering", 3.5)
name, age, dept, gpa = student
print(name)
print(age)
print(dept)
print(gpa)


scores = (75, 82, 90, 45, 67, 90, 88, 90)
total = sum(scores)
print(total)
avg = total/len(scores)
print(avg)
print(max(scores))
print(min(scores))
print(scores.count(90))
print(scores.index(90))
count = 0
for sc in scores:
    if sc >= 50:
        count += 1
print(count)

import math
point = (10,20)
x, y = point
total = sum(point)
distance = math.sqrt(x ** 2 + y**2 )
print(distance)