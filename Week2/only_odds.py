def isEven(number):
    return number %2 == 0 
def is_odd(number):
    return not isEven(number)
num = input("Please input a squence of numbers.")
# myNum = [int(n) for n in num.split()]
# for number in myNum:
#     if is_odd(number):
#         print(f"{number} is odd")
int_list= []
for n in num:
    if n != " ":
        int_list.append(int(n))
print(int_list)
# number_list = [11, 20, 42, 97, 23, 10]
for n in int_list:
    if is_odd(n):
        print(n)
