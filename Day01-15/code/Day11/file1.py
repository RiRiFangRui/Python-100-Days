"""
从文本文件中读取数据

Version: 0.1
Author: 骆昊
Date: 2018-03-13
"""

import time


def main():
    # 一次性读取整个文件内容
    with open('致橡树.txt', 'r', encoding='utf-8') as f:
        print(f.read())

    # 通过for-in循环逐行读取
    with open('致橡树.txt', mode='r') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
    print()

    # 读取文件按行读取到列表中
    with open('致橡树.txt') as f:
        lines = f.readlines()
    print(lines)
    

if __name__ == '__main__':
    main()

    
    
    
总结：

【进行逻辑判断（比如if）时，Python当中等于False的值并不只有False一个，它也有一套规则。
对于基本类型来说，基本上每个类型都存在一个值会被判定为False。
布尔型，False表示False，其他为True整数和浮点数，0表示False，其他为True
字符串和类字符串类型（包括bytes和unicode），空字符串表示False，其他为True
序列类型（包括tuple，list，dict，set等），空表示False，非空表示True
None永远表示False

作者：灵剑
链接：https://www.zhihu.com/question/48707732/answer/112233903
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。】
