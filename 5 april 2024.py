# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 10:44:24 2024

@author: 2705919
"""

#read the datafile containing survey answer
# and find out which spots wre the favourites
# by counting how many times each spot was voted for

#open the file
file = open("responses.csv")

#remove the fits(header) line
junk = file.readline()
junklist = junk.split(",")
#read the firs real data line
#data = file.readline()
#print(data)

#split the data (string) into a list
#datalist = data.split(",")

#access the first element in the datalist
#print(datalist[0])

#access the item we want
#print(datalist[4])
club_ilia_tally = 0
uncle_faih_tally= 0

for data in file:
    #split the data(string) into a list
    datalist = data.split(",")
    
    #access the item that we want
    print(datalist[4])
    
    answer = datalist[4]
    
    if answer=='Club Ilia':
        club_ilia_tally += 1
    elif answer=="Uncle Fatih's":
        uncle_faih_tally += 1
print("------------------PIZZA TALLIES-------------------")
print("Club Ilia: "+str(club_ilia_tally))
print("Uncle Fatih's: "+str(uncle_faih_tally))


