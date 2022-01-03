# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2022/1/3 0003 15:18

# 提示用户 **输入密码**，如果 **长度少于 8**，抛出 **异常**
# 1. **创建** 一个 `Exception` 的 **对象**
# 2. 使用 `raise` **关键字** 抛出 **异常对象**

def input_password():

    pwd = input("请输入长度大于8位的密码：")

    if len(pwd) >= 8:
        return pwd

    print("主动抛出异常")
    ex = Exception("密码长度不足")
    raise ex


try:
    print(input_password())
except Exception as result:
    print(result)
