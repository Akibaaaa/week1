name = input("Enter your name: ")
weight = float(input("Enter your weight in Kgs: "))
height = float(input("enter your height in meter: "))
bmi = weight/ (height**2)
bmi = round(bmi,2)
print("==========================================")
print("               BMI REPORT                 ")
print("==========================================")
print(f'''Name: {name}
Weight: {weight}
Height: {height}
 
BMI: {bmi}''')
print("==========================================")