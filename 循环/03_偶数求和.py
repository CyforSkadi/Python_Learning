# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2021/12/12 0012 20:28

# 计算 0 ~ 100 之间 所有 **偶数** 的累计求和结果
i = 0
result = 0

while i <= 100:
    if i % 2 == 0:
        print(i)
        result += i

    i += 1

print(result)
