# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2021/12/13 0013 19:55

poem = "登鹳雀楼\t 王之涣\t 白日依山尽 \t \n 黄河入海流 \t\t 欲穷千里目 \t\n 更上一层楼"

print(poem)

# 拆分字符串 返回一个列表
poem_list = poem.split()
print(poem_list)

# 合并字符串
poem_str = " ".join(poem_list)
print(poem_str)