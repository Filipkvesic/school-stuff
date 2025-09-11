#author filip kvesic
#date 11th september 2025
#question 3.programme 4 print sum of all numbers in given range
number = int(input('please enter a number: '))

for i in range(13):
    total = number * i
    print(number, '*', i,'=', total)