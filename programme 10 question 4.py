#author filip kvesic
#date 24/10/2025
#description print out every odd positioned letter in a string
string = input('please enter a string: ')
i = 0
ii = 0
empty = ''
for ii in range(0,(len(string))):
    if ii % 2 == 1:
        empty = empty + string[ii]
print(empty)
        
    