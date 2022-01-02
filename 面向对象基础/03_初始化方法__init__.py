# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2021/12/15 0015 21:33

class Cat:

    # 创建对象时设置对象属性为__init__方法的参数
    def __init__(self, new_name):
        print("这是一个初始化方法")

        # 定义猫对象具有的属性name
        self.name = new_name

    def eat(self):
        print("%s爱吃鱼" % self.name)

# 使用类名()创建对象时会自动调用初始化方法__init__
Tom = Cat("Tom")
print(Tom.name)

lazy_cat = Cat("大懒猫")
lazy_cat.eat()