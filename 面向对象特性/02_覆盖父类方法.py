# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2022/1/2 0002 14:51
class Animal:

    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")


class Dog(Animal):

    def bark(self):
        print("汪汪叫")


class XiaoTianQuan(Dog):

    def fly(self):
        print("飞")

    def bark(self):
        print("叫的跟神一样")


xtq = XiaoTianQuan()
# 重写之后，在运行时只会调用子类中重写的方法，而不再会调用父类封装的方法
xtq.bark()
