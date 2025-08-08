pet_species = "Dog"
age = 1 

if pet_species == "Dog":
    if age < 2 :
        petfood = "Puppy food"
    else:
        petfood = "Senior dog food"

if pet_species == "Cat":
    if age < 6:
        petfood = "Kitten food"
    else:
        petfood = "Senior cat food"

print("I recommend:", petfood)