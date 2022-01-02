# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2022/1/2 0002 15:01

class A:

    def __init__(self):
        self.num1 = 10
        self.__num2 = 20

    def __test(self):
        print("私有方法%d %d" % (self.num1, self.__num2))

    def test(self):
        print("公有方法%d" % self.__num2)

        self.__test()


class B(A):

    def demo(self):

        # print("访问父类私有属性%d" % self.__num2)
        # self.__test()
        self.test()
        pass


b = B()
print(b)

print(b.num1)
# **子类对象** **不能** 在自己的方法内部，**直接** 访问 父类的 **私有属性** 或 **私有方法**
# print(b.__num2)
# print(b.__test())

b.demo()
# **子类对象** 可以通过 **父类** 的 **公有方法** **间接** 访问到 **私有属性** 或 **私有方法**
b.test()
