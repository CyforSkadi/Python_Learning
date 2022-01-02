# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2021/12/15 0015 21:48

class Cat:

    def __init__(self, new_name):
        self.name = new_name

        print("%s来了" % self.name)

    # 希望使用 `print` 输出 **对象变量** 时，能够打印 **自定义的内容**，就可以利用 `__str__` 这个内置方法了
    def __str__(self):
        # `__str__` 方法必须返回一个字符串
        return "我是小猫%s" % self.name

    # 当一个对象被从内存中销毁前，会自动调用`__del__`方法
    def __del__(self):
        print("%s去了" % self.name)


Tom = Cat("Tom")
print(Tom)
