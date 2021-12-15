# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2021/12/15 0015 20:52

def sum_number(num):

    print(num)

    if num == 1:
        return
    # 递归必须要有出口，当参数满足条件时不再执行
    sum_number(num - 1)


sum_number(3)
