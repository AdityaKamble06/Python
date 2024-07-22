#Function to print binary number using recursion
def convertToBinary(n):
    if n > 1:
        convertToBinary(n//2)
    print(n % 2, end = ' ')

#Decimal number
dec = 34

convertToBinary(dec)
print()

#Output
1 0 0 0 1 0 
