#author filip kvesic
#date 11th september 2025
#question 3.programme 4 print sum of all numbers in given range
number = 0
number1 = int(input('please enter the range: '))
Number = number1 + 1
for i in range(Number):
    if (i%2 == 1):
    
        number = number + i
    else:
        pass

print(number)
