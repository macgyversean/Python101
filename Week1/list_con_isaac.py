favs = ["macgyver", "supernatural", "dick van dyke show", "hawaii five-0", "green arrow"]

def newList(list, name):
    for person in list:
        if person == name:
            list.remove(name)
            print(list)
            return list
        else: 
            list.append(name)
            print(list)
            return list

newList(favs, "macgyver")
newList(favs, "LARRY")
newList(favs, "John")