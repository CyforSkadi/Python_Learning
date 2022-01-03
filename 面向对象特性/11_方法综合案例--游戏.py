# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2022/1/3 0003 14:16

class Game(object):

    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    @staticmethod
    def show_help():
        print("帮助信息：让僵尸进入大门")

    @classmethod
    def show_top_score(cls):
        print("历史最高分：%d" % cls.top_score)

    def start_game(self):
        print("%s开始游戏" % self.player_name)


Game.show_help()
Game.show_top_score()

pvz = Game("蛋挞")
pvz.start_game()
