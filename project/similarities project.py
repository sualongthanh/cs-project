#Ken Vu
#17th april 2024
#similarities project
file = open('sfu_best_cmpt120.csv')
junk = file.readline()
counter_list = []
counter = 0
favourite = ["Starbucks","Noodle Waffle Cafe","Uncle Fatih's","Quesada (Cornerstone)"
             ,"Subway"]
highest_point = 0

for data in file:
   data_list = data.split(",")
   for choice in data_list:
       if choice in favourite:
           counter += 1
   counter_list.append(counter)
   counter = 0
   for i in range(len(counter_list)):
       for i in counter_list:
           if i > highest_point:
               highest_point = i
   if i == highest_point:
      print(data_list[1], "has the highest point")
      print(data_list[2])
      print(data_list[3])
      print(data_list[4])
      print(data_list[5])
      print(data_list[6])
      print("***************************************")