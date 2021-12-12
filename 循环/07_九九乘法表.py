# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2021/12/12 0012 20:55

# 输出九九乘法表
row = 1

while row <= 9:

    col = 1

    while col <= row:
        # 转义字符：
        # | \\ | 反斜杠符号
        # | \' | 单引号
        # | \"  | 双引号
        # | \n | 换行
        # | \t | 横向制表符
        # | \r | 回车
        print("%d * %d = %d" % (col, row, (col * row)), end="\t")
        col += 1
    print("")

    row += 1
