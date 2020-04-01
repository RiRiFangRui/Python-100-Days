"""
输入一个正整数判断它是不是素数

Version: 0.1
Author: 骆昊
Date: 2018-03-01
"""
from math import sqrt

num = int(input('请输入一个正整数: '))
end = int(sqrt(num))
is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('%d是素数' % num)
else:
    print('%d不是素数' % num)

    
a = int(input('please enter number here : '))
count = 0
i = 1
for i in range(1, a+1):
    if a % i == 0:
        count = count + 1
if count == 2 and a > 0:
    print('is sushu')
else:
    print('is not sushu')
    
    总结：随缘吧
