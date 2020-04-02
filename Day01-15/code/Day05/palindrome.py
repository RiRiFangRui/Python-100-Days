"""
判断输入的正整数是不是回文数
回文数是指将一个正整数从左往右排列和从右往左排列值一样的数

Version: 0.1
Author: 骆昊
Date: 2018-03-02
"""

num = int(input('请输入一个正整数: '))
temp = num
num2 = 0
while temp > 0:
    num2 *= 10
    num2 += temp % 10
    temp //= 10
if num == num2:
    print('%d是回文数' % num)
else:
    print('%d不是回文数' % num)

    
    
总结：num不能改变，还要和invert后的数字作比较，所以用temp赋值改变temp的数值。
    我不会反转公式。两遍了还是捋不清逻辑。数据算法结构不及格。
