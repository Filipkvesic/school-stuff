#author filip kvesic
#3rd october 2025
#find the average of the test grades and give it a letter
n = -1
total = 0
count = 0
while n!='':
    n = input('enter a number: ')
    if n.isdigit():
        total += int(n)
        count +=1
average = total/count
if average >= 90 and average <=100:
    print('A')
elif average >= 80 and average <=89:
    print('B')
elif average >= 70 and average <=79:
    print('C')
elif average >= 60 and average <=69:
    print('D')
elif average <= 59:
    print('F')