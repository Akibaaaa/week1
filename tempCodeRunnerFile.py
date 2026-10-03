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