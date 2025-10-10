#author filip kvesic
#date 10/10/2025
#description take n which is bigger than 20 as input, print numbers from 11 to n when number is multiple of 3 7 and both do random words
number = int(input('please enter a number bigger than 20: '))
if number > 20:
    print('fantastic')
else:
    print('it aint bigger than 20')
iteration = 10
 
while iteration <= number:
    iteration = iteration + 1
    if iteration %3 == 0 and iteration %7 == 0:
        print('TipsyTopsy')
    elif iteration %3 == 0:
        print('tipsy')
    elif iteration %7 == 0:
        print('topsy')
    else:
        print(iteration)
