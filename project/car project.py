#Purpose: Listing the cars have the lowest or highest mpg
#Author: Ken Vu
#Date: 9th April,2024
#***************************************
#open file
file = open("data.csv")
#remove the fits(header) line
junk = file.readline()
junklist = junk.split(",")
#set the variables
highest_mile = 0
lowest_mile = 100
miles_list = []
#*****************************************
#Main program
for data in file:
    #make the data into the list
    car_data = data.split(',')
    #change the list into integer
    miles = int(car_data[-3])
    #add the variable in the mile list
    miles_list.append(miles)
    #find the highest mile     
    if int(miles) > highest_mile:
        highest_mile = int(miles)
        miles_list = []
    #find the lowest mile
    if int(miles) < lowest_mile:
        lowest_mile = int(miles)
        miles_list = []
#Find the car that has highest mile or lowest mile  
    if miles == highest_mile:
        Make_high = car_data[0]
        Model_high = car_data[1]
        Year_high = car_data[2]
        MSRP_high = car_data[-1]
        print("The "+str(Make_high)," car, model: "+str(Model_high),", year "+str(Year_high),", MSRP: "+str(MSRP_high), end=" ")
        print("has the highest mile: "+str(highest_mile))
    if miles == lowest_mile:
        Make = car_data[0]
        Model = car_data[1]
        Year = car_data[2]
        MSRP = car_data[-1]
        print("The "+str(Make)," car, model: "+str(Model),", year "+str(Year),", MSRP: "+str(MSRP),end=" ")
        print("has the lowest mile: "+str(lowest_mile))
#*****************************************
