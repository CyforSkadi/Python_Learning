# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2022/1/3 0003 15:08

# try:
#     # 尝试执行的代码
#     pass
# except 错误类型1:
#     # 针对错误类型1，对应的代码处理
#     pass
# except 错误类型2:
#     # 针对错误类型2，对应的代码处理
#     pass
# except (错误类型3, 错误类型4):
#     # 针对错误类型3 和 4，对应的代码处理
#     pass
# except Exception as result:
#     # 打印错误信息
#     print(result)
# else:
#     # 没有异常才会执行的代码
#     pass
# finally:
#     # 无论是否有异常，都会执行的代码
#     print("无论是否有异常，都会执行的代码")

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
else:
    print("尝试成功")
finally:
    print("无论是否出现错误都会执行的代码")

print("-" * 50)
