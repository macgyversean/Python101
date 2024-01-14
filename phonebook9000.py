phonebook_dict = {
    'names': {
        'Alice': '703-493-1834',
        'Bob': '857-384-1234',
        'Elizabeth': '484-584-2923'
    }
}
print("Electronic Phone Book")
lookup = print("1. Look up an entry", 
               "2. Set an entry",
               "3. Delete an entry",
               "4. List all entries",
               "5. Quit"
               )
user_action = input("Choose an action (1/2/3/4/5): ")
if user_action == '1. look up an entry':
    search_name = input(' Enter the persons name.')
    if search_name in phonebook_dict:
        print('phone number for {search_name}: {phonebook[search_name]}')
    else:
        print('Sorry that person does not exist in this phone book please add.')