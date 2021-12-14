# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2021/12/14 0014 16:53

# 全局变量应定义在代码上方,import下方
# 全局变量命名gl_
gl_num = 199

def demo1():

    # 函数内不能修改全局变量的引用，只是新建了一个局部变量
    # num = 100

    # 若要在函数内部修改全局变量，需要使用global关键字
    global gl_num
    gl_num = 100

    print("demo1 ==> %d" % gl_num)


def demo2():

    print("demo2 ==> %d" % gl_num)


demo1()
demo2()
