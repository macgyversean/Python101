hotel = {
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

while True:
    print("\nWelcome to the Hotel!")
    print("1. Check In")
    print("2. Check Out")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        floor_number = input("Enter floor number: ")
        room_number = input("Enter room number: ")

        if floor_number in hotel and room_number in hotel[floor_number]:
            print("Room is already occupied.")
        else:
            num_occupants = int(input("Enter number of occupants: "))
            occupants = []
            for i in range(num_occupants):
                name = input(f"Enter name of occupant {i+1}: ")
                occupants.append(name)

            hotel.setdefault(floor_number, {})[room_number] = occupants
            print("Check-in successful!")

    elif choice == '2':
        floor_number = input("Enter floor number: ")
        room_number = input("Enter room number: ")

        if floor_number not in hotel or room_number not in hotel[floor_number]:
            print("Room is not occupied.")
        else:
            del hotel[floor_number][room_number]
            print("Check-out successful!")

    elif choice == '3':
        break

    else:
        print("Invalid choice. Please try again.")