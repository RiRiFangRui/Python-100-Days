"""
多重继承
- 菱形继承(钻石继承)
- C3算法(替代DFS的算法)

Version: 0.1
Author: 骆昊
Date: 2018-03-12
"""


class A(object):
    def foo(self):
        print('foo of A')

class B(A):
    pass

class C(A):
    def foo(self):
        print('foo fo C')

class D(B, C):
    pass

class E(D):
    def foo(self):
        print('foo in E')
        super().foo()
        super(B, self).foo()
        super(C, self).foo()

if __name__ == '__main__':
    d = D()
    d.foo()
    e = E()
    e.foo()

输出：
foo fo C
foo in E
foo fo C
foo fo C
foo of A
    
问题：43行输出怎么回事？
    30行 将B的父类A的foo给B，调用B类发现pass，主动过到下一个C类？我晕了 一会儿回来
    
    回来了
    https://blog.csdn.net/biexiaofei/article/details/86484177?depth_1-utm_source=distribute.
    pc_relevant.none-task-blog-OPENSEARCH-2&utm_source=distribute.pc_relevant.none-task-blog-OPENSEARCH-2
    菱形继承的拓扑

总结：https://blog.csdn.net/weixin_40636692/java/article/details/79940501  看各种类的继承。
    super(), 在子类中即使已经覆盖父类方法也可用它调用出来父类方法。
    

