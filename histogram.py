histogram = {}
word = input("Please enter a word ")
for letters in range(len(word)):
    if word[letters] in histogram:
      histogram[word[letters]] += 1
    else:
        histogram[word[letters]] = 1 
print(histogram) 