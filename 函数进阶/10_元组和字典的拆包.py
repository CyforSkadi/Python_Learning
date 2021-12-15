# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2021/12/15 0015 20:31

def demo(*args, **kwargs):

    print(args)
    print(kwargs)

# 需要将一个元组变量/字典变量传递给函数对应的参数,则需要使用拆包
# *元组变量  **字典变量
gl_num = (1, 2, 3)
gl_dictionary = {"name":"蛋挞", "age":21}

demo(*gl_num, **gl_dictionary)