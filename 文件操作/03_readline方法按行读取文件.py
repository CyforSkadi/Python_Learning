# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2022/1/4 0004 14:13

file = open("README")

while True:
    text = file.readline()
    print(text)

    if not text:
        break

file.close()
