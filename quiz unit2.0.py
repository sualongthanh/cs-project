# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 10:21:38 2024

@author: 2705919
"""

foods = ["Burger","taco",'tempura']
print(len(foods))
pickle = 10
for i in range(5):
    pickle += -1
print(pickle)

numRoses = 10
isBlue = True
isRed = True
if isBlue:
    numRoses += 5
    isRed = False
if isRed:
    numRoses += 5
else:
    numRoses +=1
print(numRoses)

score = 0
weights = [1,2,3]
for weight in weights:
    score += weight*int(input())
    print(score)