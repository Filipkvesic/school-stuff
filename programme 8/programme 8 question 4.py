#author filip kvesic
#date 10/10/2025
#description find the second largest number in a group of numbers
number = 1
copynumber = 0
iteration = 0
newnumber = 0
while number != 0:
    number = int(input('please enter a number and make it not zero pls unless you want to finish adding numbers:  '))
    if number == 0:
        print(secondmax)
        break
    if number > copynumber:
        secondmax = copynumber
        copynumber = number
    

