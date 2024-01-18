day = int(input("day (0-6)?"))
days_of_week = ("sunday", "Monday", "Tuedsday", "Wednesday", "Thursday", "Friday", "Saturday")
if 0 <= day <= 6: 
    print(days_of_week[day]) 

else :
    print ("not available. Please try again. ")