total_bill = float(input("Total bill amount? "))
service =  input("How was the service (good, fair, bad): ")
tip_percentage = {"good": .20, "fair": .15, "bad": .10}
print(tip_percentage[service])
tip_ammount = total_bill * tip_percentage[service]   
final_bill = total_bill + tip_ammount
print(tip_ammount) 
print(final_bill)