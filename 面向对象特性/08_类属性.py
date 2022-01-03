# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2022/1/3 0003 13:52

class Tool(object):

    count = 0

    def __init__(self, name):
        self.name = name

        # 通过类名.的方式可以访问类的属性或者调用类的方法
        Tool.count += 1


tool1 = Tool("斧头")
tool2 = Tool("锤子")
tool3 = Tool("刀")

print(Tool.count)
