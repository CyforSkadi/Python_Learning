# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2021/12/15 0015 19:55

def demo(num, num_list):

    print("函数开始")

    num += num
    # 列表变量调用+=本质上是在执行列表变量的extend方法，不会修改变量的引用
    num_list += num_list

    print(num)
    print(num_list)

    print("函数完成")

gl_num = 9
gl_list = [1, 2, 3]

demo(gl_num,gl_list)
print(gl_num)
print(gl_list)