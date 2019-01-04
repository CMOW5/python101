# normal for loop
animals = ['cat', 'dog', 'bird', 'fish']

for animal in animals:
  print(animal)

# modify the sequence you are iterating
for animal in animals[:]: # loop over a slice copy of the entire list
  if len(animal) > 3:
    animals.insert(0, animal)

print(animals)