#Source Code: Using if...elif...else

num = float(input("Enter a number: "))
if num > 0:
 print("Positive number")
elif num == 0:
 print("Zero")
else:
 print("Negative number")

#Output
Enter a number: 3
Positive number
-------------------------------------------------------------------------------------------------
#Source Code: Using Nested if

num = float(input("Enter a number: "))
if num >= 0:
 if num == 0:
  print("Zero")
 else:
  print("Positive number")
else:
 print("Negative number")

#Output
Enter a number: 3
Positive number
