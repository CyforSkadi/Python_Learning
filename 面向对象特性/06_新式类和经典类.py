# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2022/1/2 0002 15:25

# `object` 是 `Python` 为所有对象提供的 **基类**，提供有一些内置的属性和方法
# 为了保证编写的代码能够同时在 `Python 2.x` 和 `Python 3.x` 运行！
# 今后在定义类时，**如果没有父类，建议统一继承自 `object`**

class A(object):
    pass


print(dir(A))
