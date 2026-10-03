stud_name = input("Student Name: ")
python_score = float(input("Python Score: "))
english_score = float(input("English Score: "))
math_score = float(input("Mathematics Score: "))
avg = (python_score + english_score + math_score)/3
avg = round(avg, 2)
print("=================================================")
print("          STUDENT RESULT                         ")
print("=================================================")
print(f'''Student: {stud_name}

Python: {python_score}
Mathematics: {math_score}
------------------------------------------------
Average: {avg}

=================================================''')
