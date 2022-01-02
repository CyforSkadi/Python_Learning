# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2021/12/15 0015 21:44

class Cat:

    def __init__(self, new_name):

        self.name = new_name

        print("%s来了" % self.name)

    # 当一个对象被从内存中销毁前，会自动调用`__del__`方法
    def __del__(self):

        print("%s去了" % self.name)

Tom = Cat("Tom")
print(Tom.name)

# **生命周期**
#
# * 一个对象从调用 `类名()` 创建，生命周期开始
# * 一个对象的 `__del__` 方法一旦被调用，生命周期结束
# * 在对象的生命周期内，可以访问对象属性，或者让对象调用方法