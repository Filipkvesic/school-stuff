#author filip kvesic
#date 30 september
#description print the factorial of a given non negative integer number
number = int(input('please enter a non negative integer: '))
factorial = 1
for i in range (1, number + 1 ):
    factorial = factorial * i
print(factorial)

