histogram = {}
name = input("Please enter a word ")
for letters in range(len(name)):
    if name[letters] in histogram:
      histogram[name[letters]] += 1
    else:
        histogram[name[letters]] = 1 
print(histogram) 