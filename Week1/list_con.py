favs = ["macgyver", "supernatural", "psych", "monk", "hawaii five-0"]

def newlist(list, name):
    for show in list:
        if show == name:
            list.remove(name)
            return list
    else:
        list.append(name)
        return list
print(newlist(favs, "supernatural"))
print(newlist(favs, "chicago fire"))
