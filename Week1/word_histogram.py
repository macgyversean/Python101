histogram = {}
name = input("Please enter a sentence ")
for word in name.split():
    if word in histogram:
      histogram[word] += 1
    else:
        histogram[word] = 1 
print(histogram) 