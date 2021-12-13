# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2021/12/13 0013 19:50

poem = ["\t\n登鹳雀楼",
        "王之涣",
        "白日依山尽",
        "黄河入海流\t\n",
        "欲穷千里目",
        "更上一层楼"]

for poem_str in poem:

    # strip方法去除空白字符
    print("|%s|" % poem_str.strip().center(10, "　"))
