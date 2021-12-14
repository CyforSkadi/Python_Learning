# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2021/12/14 0014 14:34
import cards_tools

while True:

    # TODO注释用于标记需要完成的工作
    # 显示功能菜单
    cards_tools.show_menu()

    action_str = input("请选择需要执行的操作：")
    print("您选择的2"
          "操作是[%s]" % action_str)

    # 1,2,3 针对名片操作
    if action_str in ["1", "2", "3"]:

        # 开发时不希望立刻编写分支内部代码，使用pass关键字占位保证代码结构正确
        # pass
        # 新增名片
        if action_str == "1":
            # pass
            cards_tools.new_card()

        # 显示全部
        elif action_str == "2":
            # pass
            cards_tools.show_all()

        # 查询名片
        elif action_str == "3":
            # pass
            cards_tools.search_card()

    # 0 退出系统
    elif action_str == "0":

        # pass
        print("欢迎再次使用名片管理系统")
        break

    # 其他输入错误，提示用户
    else:
        print("输入错误,请重新选择")
