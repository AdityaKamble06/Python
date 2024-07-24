# Multiple exceptions as a parenthesized tuple

string = input()

try:
    num = int(input())
    print(string+num)
except (TypeError, ValueError) as e:
    print(e)

#Output
# a
# 2
