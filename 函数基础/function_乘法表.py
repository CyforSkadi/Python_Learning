# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2021/12/13 0013 14:23

def multiple_table():
    row = 1

    while row <= 9:
        col = 1

        while col <= row:
            print("%d * %d = %d" % (col, row, col * row), end="\t")
            col += 1

        print("")
        row += 1
