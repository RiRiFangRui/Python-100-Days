"""
打印各种三角形图案

*
**
***
****
*****

    *
   **
  ***
 ****
*****

    *
   ***
  *****
 *******
*********

Version: 0.1
Author: 骆昊
Date: 2018-03-01
"""

row = int(input('请输入行数: '))
for i in range(row):
    for _ in range(i + 1):
        print('*', end='')
    print()

for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()


总结：print默认（\n）是打印一行，结尾加换行。end=' '意思是末尾不换行，加空格。end='\t' 不换行
第一个三角很基础啊
第二个三角想不到
第三个三角是第二个三角变形
我看不懂嘻嘻
