#author filip kvesic
#date  9/10 2025
#description to check whether a number ends in 4 or 8
number = int(input('please enter a number:  '))
Number = number
digits = 0
minusvariable = 0
total = 0
for i in range(1, Number + 1):
    if (number < 1):
        i = Number
    else:
        number = number / 10
        digits = digits + 1

        
for i in range(digits, 0, -1):
    variable = Number // 10**(i-1)
    number1 = variable
    number1 = number1 - minusvariable
    minusvariable = variable * 10
    total = total + number1 ** digits
    
if number1 == 4:
    print('ends in 4')
elif number1 == 8:
    print('ends in 8')
else:
    print('ends in neither')
    

