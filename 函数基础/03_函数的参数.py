# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2021/12/13 0013 14:47

# 在函数名的后面的小括号内部填写参数
# 多个参数之间使用 , 分隔
def sum_2_num(num1, num2):
    """对两个数字的求和"""

    result = num1 + num2

    print("%d + %d = %d" % (num1, num2, result))

sum_2_num(10, 20)
