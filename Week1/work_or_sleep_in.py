day = int(input("day (0-6)?"))
days_of_week = ("Sunday", "Monday", "Tuedsday", "Wednesday", "Thursday", "Friday", "Saturday")
if 1 <= day <= 5: 
    print(days_of_week [day])
    print ("Go to work") 

else :
    print (days_of_week [day])
    print ("Sleep in.")