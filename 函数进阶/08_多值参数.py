# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2021/12/15 0015 20:16

# 参数名前增加一个`*`可以接收元组
# 参数名前增加两哥`*`可以接收字典
def demo(num, *args, **kwargs):

    print(num)
    print(nums)
    print(person)


demo(1, 2, 3, 5, name = "小明", age = 18)