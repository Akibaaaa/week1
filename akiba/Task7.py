destiny = input("Destination: ")
distance = float(input("Distance in Kilometers: "))
avg_speed = float(input("ENter the speed in Km/h: ")) 
time = distance / avg_speed
time_in_hrs = int(time)
time_in_min = (time - time_in_hrs) * 60

print("Destination: ", destiny)
print("Distance: ", distance)
print("Average Speed: ", avg_speed)
print("Estimated Travel Time: ", time_in_hrs,"hrs:", time_in_min ,"min")