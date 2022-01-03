# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2022/1/3 0003 15:12

# * **异常的传递** —— 当 **函数/方法** 执行 **出现异常**，会 **将异常传递** 给 函数/方法 的 **调用一方**
# * 如果 **传递到主程序**，仍然 **没有异常处理**，程序才会被终止

def demo1():
    return int(input("输入整数："))


def demo2():
    return demo1()


# 在开发中，可以在主函数中增加 **异常捕获**
try:
    print(demo2())
except Exception as result:
    print("未知错误%s" % result)
