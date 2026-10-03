#question number Four
def analyze_aqi(sensor_data):
    summary={}
    for city in sensor_data:
        readings = sensor_data[city]
        avg = sum(readings)/len(readings)
        if 0 < avg< 12:
            summary[city]= "Good"
        elif 12.1 < avg < 35.4:
            summary[city] = "Moderate"
        else:
            summary[city] = "Unhealthy"
    return summary
sensor_data ={}
no_of_cities = int(input("How many cities: "))
for i in range(no_of_cities):
    city = input("THe name of the city: ")
    no_of_readings = int(input("The number of readings: "))
    readings = []
    for j in range(no_of_readings):
        value = float(input(f"enter the reading {j+1}"))
        readings.append(value)
        sensor_data[city] = readings
result = analyze_aqi(sensor_data)
print(result)

