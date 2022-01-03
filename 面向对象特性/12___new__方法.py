# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2022/1/3 0003 14:29

class MusicPlayer(object):

    def __new__(cls, *args, **kwargs):
        # 创建对象时__new__方法会被自动调用
        print("创建对象分配空间")
        # 重写`__new__`方法一定要 return super().__new__(cls)
        return super().__new__(cls)

    def __init__(self):
        print("播放器初始化")


player = MusicPlayer()
print(player)