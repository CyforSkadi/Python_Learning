# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2022/1/3 0003 14:04

# 语法：
# @classmethod
# def 类方法名(cls):
#     pass

class Tool(object):

    count = 0

    @classmethod
    def show_tool_count(cls):
        print("工具对象的数目为%s" % cls.count)

    def __init__(self, name):
        self.name = name
        Tool.count += 1


tool1 = Tool("斧头")
tool2 = Tool("斧头")
tool3 = Tool("斧头")

Tool.show_tool_count()