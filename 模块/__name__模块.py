# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2022/1/4 0004 13:30

def say_hello():
    print("你好")


# 如果直接执行模块，得到的值为__main__
if __name__ == "__main__":
    print(__name__)

    # 文件被导入时，能够直接执行的代码不需要被执行
    print("蛋挞开发的模块")
    say_hello()
