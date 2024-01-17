def isEven(number):
  return number %2 == 0
def is_odd(number):
  return not isEven(number)

number = int(input("please input a number."))

if is_odd(number):
  print(f"{number} is odd.")
else: 
    print(f"{number} is even.")
