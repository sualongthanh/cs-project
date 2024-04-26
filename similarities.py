# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 10:59:24 2024

@author: 2705919
"""

# Description: finds out how similar two prople are by comparing
#their lists of favourite movies

# 1. Get the favourite movies for each person
angelica_favourite_movies = ['Big Hero 6', 'Inside Out', 'Wall-E']
baymax_favourite_movies = ['Big Hero 6', 'Inside Out', 'Wall-E']
#2. Initialize aa common interests counter
comon_interest_counter = 0

#3> Go through all the favourite movies of the first person
for movie in angelica_favourite_movies:
    #a. if that movie is also in the 2nd person's list
    if movie in baymax_favourite_movies:
      #Add to the common counter
        comon_interest_counter += 1
#4. Print the common interests counter to get a similarity score
print(comon_interest_counter)                           