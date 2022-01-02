# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2022/1/2 0002 13:19

class Person:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return "我的名字叫%s，体重是 %.2f 公斤" % (self.name, self.weight)

    def run(self):
        print("%s爱跑步，跑步锻炼身体" % self.name)

        self.weight -= 0.5

    def eat(self):
        print("%s是吃货，吃完这顿在减肥" % self.name)

        self.weight += 1


xiaoming = Person("小明", 75.0)

xiaoming.run()
xiaoming.eat()

print(xiaoming)

xiaomei = Person("小美", 45.0)

xiaomei.eat()
xiaomei.run()

print(xiaomei)
