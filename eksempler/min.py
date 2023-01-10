from datetime import datetime


file = open("/Users/emilpetersson/Skole/ING301/ing301public/eksempler/gpsdata/gpslogs/short.csv", "r")

lines = file.readlines()
counter = 0
gps_point = []

for line in lines:
    if counter > 0:
        gps_point.append(line)
        
    counter += 1
        


first = gps_point[0]
first_split = first.split(",")
first_timestamp = datetime.fromisoformat(first_split[0])


print(first_timestamp)
print(type(first_timestamp))




    
file.close()