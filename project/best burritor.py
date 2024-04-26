file = open("responses.csv")
Guadalupe = 0
Quesada  = 0
for data in file:
    burrito_places = data.split(',')
    answer = burrito_places[5]
    
    if answer == 'Guadalupe (MBC)':
        Guadalupe += 1
    elif answer == 'Quesada (Cornerstone)':
        Quesada  += 1

print("------------------BEST BURRITOS-------------------")
print("Guadalupe (MBC): "+str(Guadalupe))
print("Quesada (Cornerstone): "+str(Quesada))

if Guadalupe < 1:
    print("No one likes Guadalupe: ")
elif Guadalupe >= 1 and Guadalupe <5:
    print("Not bad, Guadalupe")
    
if Quesada < 1:
    print("No one likes Quesada: ")
elif Quesada >= 1 and Quesada <5:
    print("Not bad, Quesada")

if Quesada > Guadalupe:
    print("The best burritos is: Quesada")
elif Quesada < Guadalupe:
    print("The best burritos is: Guadalupe")
