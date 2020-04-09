"""
定义和使用学生类

Version: 0.1
Author: 骆昊
Date: 2018-03-08
"""


def _foo():
    print('test')


class Student(object):

    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s正在学习%s.' % (self.name, course_name))

    # PEP 8要求标识符的名字用全小写多个单词用下划线连接
    # 但是很多程序员和公司更倾向于使用驼峰命名法(驼峰标识)
    def watch_av(self):
        if self.age < 18:
            print('%s只能观看《熊出没》.' % self.name)
        else:
            print('%s正在观看岛国大电影.' % self.name)


def main():
    stu1 = Student('骆昊', 38)
    stu1.study('Python程序设计')
    stu1.watch_av()
    stu2 = Student('王大锤', 15)
    stu2.study('思想品德')
    stu2.watch_av()


if __name__ == '__main__':
    main()

    
总结：关键点：调用类时 stu1 = Student('fangrui', 24) 调出 __init__用stu1内数据初始化类。
以self开头的 self.name = name 和 self.age = age 参数可以在整个类中传递
所以调用 stu.watch_av 时可以用age写if语句
