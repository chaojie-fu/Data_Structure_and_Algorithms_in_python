from time import time
"""
In Section 5.4.2, we described four different ways to compose a long string:
(1): repeated concatenation,
(2) appending to a temporary list and then joining,
(3) using list comprehension with join,
(4) using generator comprehension with join.
Develop an experiment to test the efficiency of all four of these approaches and report your findings.
"""

string = input('INPUT THE STRING: ')
print(string)
print('\n')

# repeated concatenation
start = time()
letter_a = ''
for a in string:
    if a.isupper():
        letter_a += a
end = time()
print('letter_a = %s' % letter_a)
print('time = %f' % (end - start))
print('\n')

# appending to a temporary list and then joining
start = time()
temp_b = []
for b in string:
    if b.isupper():
        temp_b.append(b)
letter_b = ''.join(temp_b)
end = time()
print('letter_b = %s' % letter_b)
print('time = %f' % (end - start))
print('\n')

# using list comprehension with join
start = time()
letter_c = ''.join([c for c in string if c.isupper()])
end = time()
print('letter_c = %s' % letter_c)
print('time = %f' % (end - start))
print('\n')

# using generator comprehension with join
start = time()
letter_d = ''.join(c for c in string if c.isupper())
end = time()
print('letter_d = %s' % letter_d)
print('time = %f' % (end - start))
print('\n')
