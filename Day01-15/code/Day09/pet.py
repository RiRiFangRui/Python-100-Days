from abc import ABCMeta, abstractmethod


class Pet(object, metaclass=ABCMeta):

    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):
        pass


class Dog(Pet):

    def make_voice(self):
        print('%s: 汪汪汪...' % self._nickname)


class Cat(Pet):

    def make_voice(self):
        print('%s: 喵...喵...' % self._nickname)


def main():
    pets = [Dog('旺财'), Cat('凯蒂'), Dog('大黄')]
    for pet in pets:
        pet.make_voice()


if __name__ == '__main__':
    main()

    
总结：
    虽然图文关系不太大，在学习进度中pet上面一道程序出现super()函数，可以调用父类属性。https://blog.csdn.net/qq_38787214/article/details/87902291
    11行，pass，占位语句，执行程序时看到跳过。https://blog.csdn.net/violet_echo_0908/article/details/52052054
