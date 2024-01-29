guests = {
    '1': {
        '185': ['George Jefferson', 'Wheezy Jefferson'],
    },
    '2': {
        '237': ['Jack Torrance', 'Wendy Torrance'],
    },
    '3': {
        '333': ['Neo', 'Trinity', 'Morpheus']
    }
}
check = input("Are you checking in or checking out?")
floor_num = int(input("Whats your floor number?"))
room_num = int(input("Whats your room number?"))

def roomlist(list, name):
    #/ check in or out ?
    #/ floor and room# ?
    #/ if check in ?

    for check_in in list: 
        if check_in ("what's your name?"): 
            list.append(name)
            return list
    else: 
        print(guests)

        def edit_guests(check_in):
            for guest in guests:
                if check_in== guest:
                    guests.remove(check_in)
                    return guests
            else:
                guests[check_in] = check_in
                return guests
    result = edit_guests(name)
    
    print(result)