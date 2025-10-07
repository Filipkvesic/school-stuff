#author filip kvesic
#date 30 september
#description print the total number of digits in a number
number = int(input('please enter a number:  '))
Number = number
digits = 0
minusvariable = 0
total = 0
for i in range (1, Number + 1):
    if (number < 1):
        i = Number
    else:
        number = number / 10
        digits = digits + 1
        
for i in range (digits, 0, -1):
    variable = Number // 10**(i-1)
    number1 = variable
    number1 = number1 - minusvariable
    minusvariable = variable * 10
    total = total + number1 ** digits
if Number == total:
    print('your number is an armstrong number')
elif Number != total:
    print('its not an armstrong number')