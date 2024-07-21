#Program to check Armstrong numbers in a certain interval 

lower = 100
upper = 2000

for num in range(lower, upper + 1):
    #order of numeber
    order = len(str(num))

    #intialize sum
    sum = 0

    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    if num == sum:
        print(num)

#Output
153
370
371
407
1634
