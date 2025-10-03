#author filip kvesic
#date 3rd of october
#description write every number up to the given number skipping every multiple of 5
number = int(input('please enter a number: '))
iteration = 0
while iteration < number:
    iteration = iteration + 1
    if iteration % 5 == 0:
        continue
    print(iteration)
    