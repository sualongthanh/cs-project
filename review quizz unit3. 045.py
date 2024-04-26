response = "I LOVE COFFEE!!"
words = response.lower().split(" ")
if "coffee" in words or "starbucks" in words:
    print("Caffeine junkie, eh?")
else:
    print("Hmmmm...")
    
pets = "cats, dogs, birds"
petslist = pets.split(",")
print("cats"in petslist)
print("dogs"in petslist)