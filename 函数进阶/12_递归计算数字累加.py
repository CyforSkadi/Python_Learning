# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2021/12/15 0015 20:57

def sum_number(num):

    # 出口
    if num == 1:

        return 1

    # 假设sum_number能够正确处理1...num-1的累加结果
    temp = sum_number(num - 1)

    return num + temp


print(sum_number(950))
