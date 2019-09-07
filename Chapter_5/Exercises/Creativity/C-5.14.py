"""
The shuffle method, supported by the random module, takes a Python list and rearranges it so that every possible
ordering is equally likely. Implement your own version of such a function. You may rely on the randrange(n) function of
the random module, which returns a random number between 0 and n-1 inclusive.
"""


from random import randrange
string = input('Input the string: ')
length = len(string)
order = [i for i in range(length)]
reorder = [0] * length
for i in range(length - 1):   # reorder index
    index = randrange(length - i - 1)
    reorder[i] = order[index]
    order.pop(index)
reorder[length - 1] = order[0]
print(reorder)

restring = [None] * length
for j in range(length):
    restring[j] = string[reorder[j]]
print(''.join(restring))
