"""
输入非负整数n计算n!

Version: 0.1
Author: 骆昊
Date: 2018-03-01
"""

n = int(input('n = '))
result = 1
for x in range(1, n + 1):
    result *= x
print('%d! = %d' % (n, result))

n = int(input('please enter integer: '))
j = 1
for i in range(1, n+1):
    j = i*j
print(j)

总结：range(1,n+1) 才能加到n
