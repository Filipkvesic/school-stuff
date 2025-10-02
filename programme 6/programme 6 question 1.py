#author filip kvesic
#2nd october 2025
#find the average of the numbers given by user
n = -1
total = 0
count = 0
while n!='':
    n = input('enter a number: ')
    if n.isdigit():
        total += int(n)
        count +=1
print('average is: ', total/count)
    
   
