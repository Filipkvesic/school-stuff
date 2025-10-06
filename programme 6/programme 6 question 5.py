#author filip kvesic
#date 6 ocotber 2025
#description 1 n squared using while loop, it should stop the loop if iteration count is 50
n = int(input('please enter a number: '))
N = n ** 2
Iteration = 0
while Iteration <= 50:
    Iteration = Iteration + 1
    print(Iteration)
    if Iteration == N or Iteration >= 50:
        break
