# Example 1: Using the | Operator

dict_1 = {1:'a', 2:'b'}
dict_2 = {2:'c', 4:'d'}

print(dict_1 | dict_2)

#Output
# {1: 'a', 2: 'c', 4: 'd'}

# Example 2: Using the ** Operator

dict_1 = {1:'a', 2:'b'}
dict_2 = {2:'c', 4:'d'}

print({**dict_1, **dict_2})

#Output
# {1: 'a', 2: 'c', 4: 'd'}
