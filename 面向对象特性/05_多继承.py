# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2022/1/2 0002 15:15

# **开发时，应该尽量避免这种容易产生混淆的情况！** —— 如果 **父类之间** 存在 **同名的属性或者方法**，应该 **尽量避免** 使用多继承

class A:

    def test(self):
        print("test方法")


class B:

    def demo(self):
        print("demo方法")


class C(A, B):

    pass


c = C()
c.test()
c.demo()

# **内置属性** `__mro__` 可以查看 **方法** 搜索顺序
print(C.__mro__)