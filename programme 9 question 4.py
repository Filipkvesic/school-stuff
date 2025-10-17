#author filip kvesic
#date 17/10/2025
#description count how many times a string appears in a word
string = input('please just say anything: ')
character = input('enter a single character so i can count it: ')
stringamount = 0
i = 0
String = len(string)
for i in range(0,String,1):
    if character == string[i]:
        stringamount += 1
print(stringamount)