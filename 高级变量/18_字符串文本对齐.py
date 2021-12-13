# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2021/12/13 0013 19:43

poem = ["登鹳雀楼",
        "王之涣",
        "白日依山尽",
        "黄河入海流",
        "欲穷千里目",
        "更上一层楼"]

for poem_str in poem:
        # 居中对齐
        # print("|%s|" % poem_str.center(10, "　"))

        # 右对齐
        # print("|%s|" % poem_str.rjust(10, "　"))

        # 左对齐
        print("|%s|" % poem_str.ljust(10, "　"))