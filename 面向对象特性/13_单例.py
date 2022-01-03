# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2022/1/3 0003 14:36

# **单例** —— 让 **类** 创建的对象，在系统中 **只有** **唯一的一个实例**
class MusicPlayer(object):

    init_flag = False
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)

        return cls.instance

    def __init__(self):
        # 让 ** 初始化动作 ** 只被 ** 执行一次 **
        if MusicPlayer.init_flag:
            return

        print("初始化播放器")

        MusicPlayer.init_flag = True


player1 = MusicPlayer()
print(player1)

player2 = MusicPlayer()
print(player2)
