def isEven(number):
    return number %2 == 0 
def is_odd(number):
    return not isEven(number)
num = (input("please input a sequence of numbers."))
# i do not understand // 
myNum = [int(n) for n in num.split()]
for number in myNum:
    if is_odd(number):
        print("")
    else:
        print(f"{number} is even.")
