# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2022/1/2 0002 14:21

class Women:

    def __init__(self, name):

        self.name = name
        self.__age = 18

    def __secret(self):
        print("%s的年龄是%d" % (self.name, self.__age))


xuanza = Women("璇砸")
# print(xuanza.age)
# xuanza.__secret()

# 伪私有
print(xuanza._Women__age)
xuanza._Women__secret()
