"""
面向对象版本的猜数字游戏

Version: 0.1
Author: 骆昊
Date: 2018-03-08
"""

from random import randint


class GuessMachine(object):

    def __init__(self):
        self._answer = None
        self._counter = None
        self._hint = None

    def reset(self):
        self._answer = randint(1, 100)
        self._counter = 0
        self._hint = None

    def guess(self, your_answer):
        self._counter += 1
        if your_answer > self._answer:
            self._hint = '小一点'
        elif your_answer < self._answer:
            self._hint = '大一点'
        else:
            self._hint = '恭喜你猜对了'
            return True
        return False

    @property
    def counter(self):
        return self._counter

    @property
    def hint(self):
        return self._hint


if __name__ == '__main__':
    gm = GuessMachine()
    play_again = True
    while play_again:
        game_over = False
        gm.reset()
        while not game_over:
            your_answer = int(input('请输入: '))
            game_over = gm.guess(your_answer)
            print(gm.hint)
        if gm.counter > 7:
            print('智商余额不足!')
        play_again = input('再玩一次?(yes|no)') == 'yes'

        
        
        
  总结：随机数radiant的产生        self._answer = randint(1, 100)
        思考类中的函数如何分类
        在初始化中 __init__ 设置传递参数，应考虑用户输入，传递，计数，等多方面。写出的程序越简单越好
        
        @property有类似private的含义，保证属性不能通过赋值的方法修改。会报错can‘t attribute, 但可通过setter getter deleter 进行ACCESS
        如下
          def width(self):
            return self.true_width
        @width.setter
         def width(self, input_width):
            self.true_width = input_width
