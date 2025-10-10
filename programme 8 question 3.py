#author filip kvesic
#date 10/10/2025
#description find the largest number in a group of numbers
number = 1
copynumber = 0
iteration = 0
while number != 0:
    number = int(input('please enter a number and make it not zero pls:  '))
    if iteration == 0:
        copynumber = number
    if number > copynumber:
        copynumber = number
    iteration = iteration + 1
print(copynumber)
    
    