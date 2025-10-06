#author filip kvesic
#date 6 october 2025
#description keep taking numbers until it all adds up to 50
total = 0
while total <= 50:
    numbers = int(input('keep giving me numbers: '))
    total = total + numbers
    if total > 50:
        break
    