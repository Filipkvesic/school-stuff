#author filip kvesic
#date 30 september
#description print the total number of digits in a number
number = int(input('please enter a number:  '))
Number = number
digits = 0
for i in range (1, Number + 1):
    if (number < 1):
        i = Number
    else:
        number = number / 10
        digits = digits + 1
        
print(digits)