# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2021/12/14 0014 16:30

def test(num):

    print("在函数内部%d对应内存地址是%d" % (num, id(num)))

    result = "hello"

    print("函数返回数据的内存地址是%d" % id(result))

    return result

a = 10

print("a保存的地址是%d" % id(a))

# 调用函数时本质上是调用实参保存数据的引用
b = test(a)

# 函数返回本质上是返回结果的引用
print("%s的内存地址是%d" % (b, id(b)))
