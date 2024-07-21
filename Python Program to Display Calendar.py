#Program to display calender of the given month and year

#importing calender module
import calendar

yy = 2006 #year
mm = 9   #month

#To take month and year input from the user
#yy = int(input("Enter year: "))
#mm = int(input("Enter month: "))

#Display the calender
print(calendar.month(yy, mm))

#Output
   September 2006
Mo Tu We Th Fr Sa Su
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30
