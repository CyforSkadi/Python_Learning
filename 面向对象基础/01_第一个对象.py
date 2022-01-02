# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2021/12/15 0015 21:18


class Cat:

    # 第一个参数必须是 `self`
    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫爱喝水")


# 创建对象 对象变量 = 类名()
Tom = Cat()

# 给对象增临时加属性，但不推荐使用
Tom.name = "Tom"

Tom.eat()
Tom.drink()

# 使用`print`输出对象变量，默认情况下，是能够输出这个变量引用的对象是由哪一个类创建的对象，
# 以及在内存中的地址（十六进制表示）
print(Tom)
# 十进制地址
print("%x" % id(Tom))

