"""
输出2~99之间的素数

Version: 0.1
Author: 骆昊
Date: 2018-03-02
"""

import math

for num in range(2, 100):
    is_prime = True
    for factor in range(2, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=' ')

        
    for num in range(1,101):
    j = 0
    for i in range(1, num+1):
        if num%i == 0:
            j += 1
    if j == 2:
        print (num)
        
        
        
  总结：素数前两天，用count计数如果数了两次就没有其它公约数
