#Python Program to Find Numbers Divisible by Another Number

#Take a list of numbers
my_list = [12,65,54,39,102,339,221,]

#use anonymous function to filter
result = list(filter(lambda x: (x % 13 == 0),my_list))

#Display the result
print("Numbers divisible by 12 are", result)

#Output
Numbers divisible by 12 are [65, 39, 221]