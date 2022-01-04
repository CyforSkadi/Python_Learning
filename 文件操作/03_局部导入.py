# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2022/1/4 0004 13:19

from 测试模块1 import Dog
from 测试模块2 import say_hello as module2_say_hello
# 导入同名函数时后导入的函数会覆盖先导入的函数，可以通过别名来区分
from 测试模块1 import say_hello

say_hello()
module2_say_hello()
dog = Dog()
print(dog)
