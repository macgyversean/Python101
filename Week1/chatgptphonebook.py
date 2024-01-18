# Step 1: Create an empty dictionary to store phonebook entries
phonebook = {}

# Step 2: Start a loop
while True:
    # Step 3: Prompt user for action
    user_action = input("Choose an action (lookup/set/delete/list/quit): ").lower()

    # Step 4: Conditional statements
    if user_action == 'lookup':
        # Step 5: Look up an entry
        search_name = input("Enter the person's name: ")
        if search_name in phonebook:
            print(f"Phone number for {search_name}: {phonebook[search_name]}")
        else:
            print(f"{search_name} not found in the phonebook.")
    
    elif user_action == 'set':
        # Step 6: Set an entry
        set_name = input("Enter the person's name: ")
        set_number = input("Enter the person's phone number: ")
        phonebook[set_name] = set_number
        print(f"Entry for {set_name} set successfully.")
    
    elif user_action == 'delete':
        # Step 7: Delete an entry
        delete_name = input("Enter the person's name to delete: ")
        if delete_name in phonebook:
            del phonebook[delete_name]
            print(f"Entry for {delete_name} deleted successfully.")
        else:
            print(f"{delete_name} not found in the phonebook.")
    
    elif user_action == 'list':
        # Step 8: List all entries
        print("All entries in the phonebook:")
        for name, number in phonebook.items():
            print(f"{name}: {number}")
    
    elif user_action == 'quit':
        # Step 9: Quit the program
        print("Exiting the phonebook program.")
        break
    
    else:
        print("Invalid action. Please choose from 'lookup', 'set', 'delete', 'list', or 'quit'.")
