# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2021/12/12 0012 19:58

# 1. 从控制台输入要出的拳 —— 石头（1）／剪刀（2）／布（3）
# 2. 电脑 **随机** 出拳 —— 先假定电脑只会出石头，完成整体代码功能
# 3. 比较胜负

# 导入随机数模块 random
# 导入工具包放在文件顶部
import random

player = int(input("请输入出什么(石头（1）／剪刀（2）／布（3）)："))

# randint(a, b)函数返回[a,b]之间的随机整数
computer = random.randint(1, 3)

print("玩家选择%d - 电脑选择%d" % (player, computer))

if ((player == 1 and computer) == 2
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):

    print("玩家胜利！")
elif player == computer:
    print("平局！")
else:
    print("电脑胜利！")
