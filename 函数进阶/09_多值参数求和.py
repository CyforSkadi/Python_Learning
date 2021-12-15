# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2021/12/15 0015 20:20

def sum_numbers(*args, **kwargs):

    num = 0

    print(args)
    for n in args:
        num += n

    return num

result = sum_numbers(1, 2, 3, 4, 5)
print(result)