#author filip  kvesic
#date 8/10/ 2025
#description convert decimal to binary


number = int(input('give a number to convert to binary: '))
combined = ""
while number != 0:
    if (number%2 == 1):
        remainder = number%2
        number = (number // 2) 
        print(int(remainder))
    elif (number%2 == 0):
        remainder = number%2
        number = number / 2
        print(int(remainder))
    remainder = int(remainder)
    combined += str(remainder)
    backward = combined[::-1]
   
   
print(backward)