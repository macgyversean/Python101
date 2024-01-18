ramit = {
    'name': 'Ramit',
    'email': 'ramit@gmail.com',
    'interests': ['movies', 'tennis'],
    'friends': [
        {
        'name': 'Jasmine',
        'email': 'jasmine@yahoo.com',
        'interests': ['photography', 'tennis']
        },
        {
        'name': 'Jan',
        'email': 'jan@hotmail.com',
        'interests': ['movies', 'tv']
        }
    ]

}

    # you want to create a variable [call it count] and set it equal to zero
    # copy the dic (x)
    # for friend in x["friends"]
        # count will increment in the loop
    # x["new_key"] = count
def countFriends(x):
    count = 0 
    new_dictionary = x.copy()
    for friend in new_dictionary["friends"]:
        count += 1
    new_dictionary["friends_count"] = count
    print(new_dictionary)
    return new_dictionary
    
    # total_friends= countFriends(ramit)
    # print("Total number of friends: {total_friends}")



countFriends(ramit)
# countFriends({
#     "a": "hello",
#     "b": "Goodbye",
# })