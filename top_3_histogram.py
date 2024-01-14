dict = {}
user_input = input("please enter a sentence")
for word in user_input.split():
    word = word.lower()
    if word in dict:
        dict[word] += 1
    else:
        dict[word] = 1 
sorted_dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)
top_3 = sorted_dict[:3]
print ("top 3 words:")
for word, frequency in top_3:
    print (f'{word}: {frequency}')