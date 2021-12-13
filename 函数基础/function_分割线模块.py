# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2021/12/13 0013 15:16

def print_line(char, times):
    """
    打印一行分割线
    :param char: 使用的字符
    :param times: 使用的次数
    :return:
    """
    print(char * times)
    return


def print_lines(char, times):
    """
    打印多行分割线
    :param char: 使用的字符
    :param times: 使用的次数
    :return:
    """
    row = 0
    while row < 5:
        print_line(char, times)
        row += 1
    return

name = "蛋挞不能吃"
