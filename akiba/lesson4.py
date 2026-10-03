# Temperature station
ans = input("Which parameter do you want to convert celisus(C) or fahrenheit(F)?")
if  ans.lower() == 'c':
    temp_celsius = float(input("Enter the temperature in celisus: "))
    temp_fahreniet = (temp_celsius * (9/5)) + 32
    print(f"celisus: {temp_celsius} °C")
    print(f"Fahrenhiet: {temp_fahreniet} F")
elif ans.lower() == 'f':
    temp_fahren = float(input("Enter the temprature in fahreniet: "))
    temp_cel = (temp_fahren - 32) * 5/9
    print(f"Fahrenhiet: {temp_fahren} F")
    print(f"celisus: {temp_cel} °C")
else:
    print("Invlaid letter choose only 'c' or 'f'.")



