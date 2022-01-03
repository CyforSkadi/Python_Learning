# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2022/1/3 0003 13:39

class Dog(object):

    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s蹦蹦跳跳的玩耍" % self.name)


class XiaoTianQuan(Dog):

    def game(self):
        print("%s飞到天上玩耍" % self.name)


class Person(object):

    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        print("%s和%s快乐地玩耍" % (self.name, dog.name))

        dog.game()


wangcai = Dog("旺财")
xtq = XiaoTianQuan("哮天犬")
xiaoming = Person("小明")

xiaoming.game_with_dog(wangcai)
xiaoming.game_with_dog(xtq)
