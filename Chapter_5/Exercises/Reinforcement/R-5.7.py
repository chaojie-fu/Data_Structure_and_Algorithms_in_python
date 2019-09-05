import random
"""
Let A be an array of size n>=2 containing integers from 1 tto n-1, inclusive, with exactly one repeated.
Describe a fast algorithm for finding the integer in A that is repeated.
"""
n = int(input('The size of array? '))
# 数组中元素的个数

# 初始化数组
A = [x for x in range(1, n)]
index = random.randint(0, n-1)
number = random.randint(0, n-1)
A.insert(index, number)
random.shuffle(A)
print(A)
B = A
# 初始化数组结束

# 算法：类似于冒泡排序
num = -1
for i in range(n):
    for j in range(n-1-i):
        if A[j+1] > A[j]:
            A[j+1], A[j] = A[j], A[j+1]
        elif A[j+1] == A[j]:
            num = A[j]
            break
    if num != -1:
        break
print(num)
