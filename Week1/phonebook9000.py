phonebook_dict = {
    'names': {
        'Alice': '703-493-1834',
        'Bob': '857-384-1234',
        'Elizabeth': '484-584-2923'
    }
}
print("Electronic Phone Book")
print("======================")
lookup = print("1. Look up an entry", 
               "2. Set an entry",
               "3. Delete an entry",
               "4. List all entries",
               "5. Quit"
               )
user_action = int(input("What do you want to do (1-5)? "))
 for  user_action in phonebook_dict['names']:
    user_action == 1: 
    search = input("Name: ")
    print()