print("hello")

def reccc(num):
    if num == 0:
        return 1
    else:
        return num * reccc(num -1)
def main():
    num = int (input("enter the number: "))
    print(reccc(num))

main()


def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    elif num > 1:
        return fib(num - 1) + fib(num - 2)
    else: 
        return "invalid input"
#print(fib(5))
n = 5
fib_seq = [fib(i) for i in range(n)]
print(f"first {n} fibonnacci numbers: {fib_seq} {fib(n)}")
def fib(N):
    num = []
    a, b=0, 1
    for i in range(n):
        num.append(a)
        a, b= b, a + b
    return num
n =10
print(f"first {n} fibonnacci numbers: (i) {fib(n)}")

def fac(n):
    fact = 1
    for i in range(1,n):
        fact  = fact * i
    return fact
print(fac(5))


for i in range (3):
    for j in range(1,4):
        print(i+j, end="")
    print()



for i in range(3):
    for j in range (1,5):
        print("[]", end= " ")
    print()

word = "banana"
index = 0
for letter in word:
    print(letter)
while (index < len(word)):
    print(word[index])
    index+=1

s ='Monty python'
print(s[0:2])
print(s[:2])
print(s[5:])

w = "ABCDEFGHIJKLM"
print(len(w))

word = "Applaplle"
count = 0
for letter in word:
    if letter.lower() == 'a':
        count +=1
print(count)

word = "banana"
for i in word:
    if 'a' in word:
       print(True)


word= input("Enter the word: ")
if word < 'banana':
    print("your word,"+word+" comes before banana.")
elif word > 'banana':
    print("your word,"+word+" comes after banana.")
else:
    print('bananas')
print(word.index('l'))

word ="a one, a two, a three"
print (word.split(','))

import string
words = ["it's", 'rainy', 'today!', "isn't", 'it?']
for i in words:
    print(i.strip(string.punctuation))




def assess_irrigation(fields, target_moisture):
    summary = {
        "Immediate Watering": 0,
        "Optimal": 0,
        "Over-watered": 0
    }

    for field in fields:
        moisture = field["moisture_percentage"]

        if moisture < 30:
            summary["Immediate Watering"] += 1

        elif moisture <= 60:
            summary["Optimal"] += 1

        else:
            summary["Over-watered"] += 1

    return summary

fields = []

number_of_fields = int(input("How many fields do you want to enter? "))

for i in range(number_of_fields):
    field_name = input(f"Enter the name of field {i + 1}: ")
    moisture = float(input(f"Enter moisture percentage for {field_name}: "))

    field = {
        "field_name": field_name,
        "moisture_percentage": moisture
    }

    fields.append(field)


# Get target moisture
target_moisture = float(input("Enter target moisture percentage: "))

# Assess the fields
result = assess_irrigation(fields, target_moisture)

# Display the result
print("\nIrrigation Summary:")
print(result)







def assess_irrigation(fields, target_moisture):
    summary ={
        "immediate watering": 0,
        "optimal": 0,
        "Over-watered": 0
    }
    for field in fields:
        moisture = field["moisture"]
        if moisture < 30:
            summary["immediate watering"]+=1
        elif moisture <=60:
            summary["optimal"]+=1
        else:
            summary["Over-watered"]+=1
    return summary
fields = []
numberOfFields = int(input("enter the number of fields:"))
for i in range (numberOfFields):
    fieldName = input(f"Name of field{i+1}:")
    moisture = float(input(f"Moisture percentage for field {i+1}:"))
    field = {
        "fieldName": fieldName,
        "moisture" : moisture}
    fields.append(field)
target_moisture = float(input("Enter target moisture percentage: "))


result = assess_irrigation(fields, target_moisture)

# Display the result
print("\nIrrigation Summary:")
print(result)

scores_dict = {"student Name": student_name,
               "student score": scores}
attendance_dict = {"student Name": student_name,
                   "student attendance": attendance}
eligible_students = []


def check_exam_eligibility(scores_dict, attendance_dict):
    eligible_students = []
    for student in scores_dict:
        student_name = student["student Name"]
        scores = student["student score"]
        avg = sum(scores)/len(scores)
        for attendance in attendance_dict:
            if attendance["student Name"] == student_name:
                atten = attendance["student attendance"]
                if avg >= 85 and atten >=90:
                    eligible_students.append(student_name)
    return eligible_students

scores_dict = []
attendance_dict = []
numberofstudents = int(input("the numbe of dtudents:"))
for i in range(numberofstudents):
    student_name = input("enter the students name")
    scores = []   
    numberofexams = int(input("how many exams")) 
    for j in range (numberofexams):
        score = float(input("enter score:"))
        scores.append(score)
    attendance = float(input("entr attendance percentage for {student_name}:"))
    scores_dict.append({"student Name": student_name, "student score": scores })
    attendance_dict.append({"student Name": student_name, "student attendance": attendance})
result = check_exam_eligibility(scores_dict, attendance_dict)
print(result)


patient_record= {"name": ,
                 "heart_rate": ,
                 "systolic_bp": }

def triage_patients(patient_list):
    summary = {
        "critical":0,
        "monitor" : 0,
        "stable" : 0
    }
    for patient in patient_list:
        heart_rate = patient["heart_rate"]
        systolic_bp = patient["systolic_bp"]

        if heart_rate > 120 or systolic_bp > 180:
            summary["critical"] +=1
            patient["status"] = "critical"
        elif heart_rate >= 100 and heart_rate <= 120:
            summary["monitor"] +=1
            patient["status"] = "monitor"
        else: 
            summary["stable"] +=1
            patient["status"] = "stable"
    return patient_list,summary
patient_list=[]
no_of_patients = int(input("enter the number of patients: "))
for i in range(no_of_patients):
    patient_name = input("enter the patient name:")
    heart_rate = int(input("enter the patients heart rate:"))
    systolic_bp = int(input("enter the patients systolic_bp:"))
    patient ={"patient name": patient_name,
              "heart_rate": heart_rate,
              "systolic_bp": systolic_bp}
    patient_list.append(patient)

result = triage_patients(patient_list)
print(result)


#sensordata= {"city_name": x,
                "listofPm": [list]}
def analyze_aqi(sensordata):
    summary = {}
    for city in sensordata:
        readings = sensordata[city]
        avg = sum(readings)/len(readings)
        if 0<avg<12:
            summary[city] = "Good"
        elif 12.1<avg<35.4:
            summary[city] = "Moderate"
        else:
            summary[city] = "Unhealthy"
    return summary
sensordata = {}
no_of_cities = int(input("enter the number of cities: "))
for i in range(no_of_cities):
    city = input("enter the city name:")
    no_of_readings = int(input("how many readings"))
    readings = []
    for j in range(no_of_readings):
        value = float(input("enter the pm2.5 value:"))
        readings.append(value)
    sensordata[city] = readings
result = analyze_aqi(sensordata)
print(result)


def balance_workload(servers):

    overloaded_servers = []

    for server_id, cpu, memory in servers:

        if cpu > 85 or memory > 90:
            overloaded_servers.append(server_id)

    return overloaded_servers


servers = []

number_of_servers = int(input("Enter the number of servers: "))

for i in range(number_of_servers):

    server_id = input("Enter server ID: ")
    cpu = float(input("Enter CPU usage: "))
    memory = float(input("Enter memory usage: "))

    server = (server_id, cpu, memory)

    servers.append(server)


result = balance_workload(servers)

print(result)




def generate_reorder_list(inventory, min_threshold):

    reorder_list = {}

    for item, stock in inventory.items():

        if stock < min_threshold:

            reorder_quantity = 100 - stock

            reorder_list[item] = reorder_quantity

    return reorder_list


inventory = {}

number_of_items = int(input("Enter the number of items: "))

for i in range(number_of_items):

    item = input("Enter item name: ")
    stock = int(input("Enter current stock: "))

    inventory[item] = stock


min_threshold = int(input("Enter minimum stock threshold: "))

result = generate_reorder_list(inventory, min_threshold)

print(result)

    
def detect_suspicious_activity(transactions, baseline_avg):

    suspicious = []

    for amount in transactions:

        if amount > 3 * baseline_avg or amount > 10000:
            suspicious.append(amount)

    total = sum(suspicious)

    print("Suspicious transactions:", suspicious)
    print("Total suspicious transaction volume:", total)


transactions = []

number_of_transactions = int(input("Enter the number of transactions: "))

for i in range(number_of_transactions):

    amount = float(input("Enter transaction amount: "))

    transactions.append(amount)


baseline_avg = float(input("Enter baseline average: "))

detect_suspicious_activity(transactions, baseline_avg)






sensor_data = {
    "city": city,
    "valueofpm": value
}

def analyze_aqi(sensor_data):
    summary ={
        "Good":0,
        "Moderate": 0,
        "Unhealthy": 0
    }
    for city in sensor_data:
        city= summary["city"]
         
