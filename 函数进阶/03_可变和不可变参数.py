# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2021/12/15 0015 19:45

# 无论传递的参数是可变还是不可变
# 只要针对参数使用赋值语句，会在函数内部修改局部变量的引用，不会影响到外部变量的引用
def demo(num, num_list):

    print("函数内部代码")

    num = 100
    num_list = [1, 2, 3]

    print(num)
    print(num_list)
    print("函数执行完成")

gl_num = 99
gl_num_list = [4, 5, 6]
demo(gl_num,gl_num_list)
print(gl_num)
print(gl_num_list)
