# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2022/1/3 0003 14:58

try:
    num = int(input("请输入一个整数："))

    result = 8 / num

    print(result)
# 捕获错误类型
except ZeroDivisionError:
    print("除0错误")
except ValueError:
    print("请输入正确整数")
# 捕获未知错误
except Exception as result:
    print("未知错误%s" % result)
