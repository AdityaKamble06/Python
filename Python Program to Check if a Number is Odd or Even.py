#Python program to check if the number is odd or even
#A number is even if division by 2 gives a reaminder of 0.
#If the remainder is 1, it is an odd number.

num = int(input("Enter a number: "))
if(num % 2) == 0:
 print("{0} is Even.".format(num))
else:
 print("{0} is Odd.".format(num))

#Output
Enter a number: 2
2 is Even.