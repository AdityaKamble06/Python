#Program ro check if a string is palindrome or not

my_str = 'ADITYA'

#make it suitable for caseless comparison
my_str = my_str.casefold()

#reverse the string
rev_str = reversed(my_str)

#check if the string is equal to its reverse
if list(my_str) == list(rev_str):
    print("The string is a polindrome.")
else:
    print("The string is not a palindrome.")

#Output
The string is not a palindrome.
