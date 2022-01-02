# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2022/1/2 0002 14:37

# class 类名(父类名):

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


class Cat(Animal):

    def catch(self):
        print("抓老鼠")


xtq = XiaoTianQuan()
xtq.fly()
xtq.bark()
xtq.eat()
# xtq.catch()
