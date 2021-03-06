# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2021/12/14 0014 14:34

# 记录所有名片字典
card_list = []


def show_menu():
    """
    显示菜单
    :return: void
    """
    print("*" * 50)
    print("欢迎使用【名片管理系统】V 1.0")
    print("")
    print("1. 新增名片")
    print("2. 显示全部")
    print("3. 查询名片")
    print("")
    print("0. 退出系统")
    print("*" * 50)


def new_card():
    """
    新增名片
    :return:void
    """
    print("-" * 50)
    print("新增名片")

    # 提示用户输入名片信息
    name_str = input("请输入姓名：")
    phone_str = input("请输入电话：")
    qq_str = input("请输入qq号码：")
    email_str = input("请输入邮箱：")

    # 使用用户输入的信息建立名片字典
    card_dict = {
        "name": name_str,
        "phone": phone_str,
        "qq": qq_str,
        "email": email_str
    }

    # 将名片字典添加到字典中
    card_list.append(card_dict)
    # print(card_list)

    # 提示用户添加成功
    print("添加 %s 的名片成功！" % name_str)


def show_all():
    """
    显示所有名片
    :return: void
    """
    print("-" * 50)
    print("显示所有名片")

    # 判断是否存在名片记录，如果没有，提示用户并返回
    if len(card_list) == 0:

        print("当前无名片记录!")
        return

    # 打印表头和分割线
    for name in ["姓名", "电话", "qq", "邮箱"]:

        print(name, end="\t\t")

    print("")
    print("=" * 50)

    # 遍历名片列表
    for card_dict in card_list:

        print("%s\t\t%s\t\t%s\t\t%s\t\t" % (card_dict["name"],
                                           card_dict["phone"],
                                           card_dict["qq"],
                                           card_dict["email"]))


def search_card():
    """
    查询名片
    :return:void
    """
    print("-" * 50)
    print("查询名片")

    # 用户输入查询的名片
    find_name = input("请输入需要查询的姓名：")

    for card_dict in card_list:

        if card_dict["name"] == find_name:

            # 输出表头和分割线
            for name in ["姓名", "电话", "qq", "邮箱"]:
                print(name, end="\t\t")
            print("")
            print("=" * 50)

            # 输出查询到的名片
            print("%s\t\t%s\t\t%s\t\t%s\t\t" % (card_dict["name"],
                                                card_dict["phone"],
                                                card_dict["qq"],
                                                card_dict["email"]))

            # 针对找到的名片进行修改和删除等操作
            deal_card(card_dict)

            break

    else:

        print("未找到%s!" % find_name)


def deal_card(find_dict):
    """
    修改或删除名片
    :param find_dict:需要操作的名片字典
    :return: void
    """
    # print(find_dict)
    select_str = input("请选择要执行的操作："
                       "1.修改 2.删除 0.返回上级菜单")

    if select_str == "1":

        find_dict["name"] = input_card_info(find_dict["name"], "姓名(回车不修改)：")
        find_dict["phone"] = input_card_info(find_dict["phone"], "电话(回车不修改)：")
        find_dict["qq"] = input_card_info(find_dict["qq"], "qq:(回车不修改)")
        find_dict["email"] = input_card_info(find_dict["email"], "邮箱(回车不修改)：")

        print("修改成功！")

    elif select_str == "2":

        # print("删除名片")
        card_list.remove(find_dict)
        print("删除成功！")


def input_card_info(dict_value, tip_message):
    """
    输入名片信息
    :param dict_value: 字典中原有值
    :param tip_message: 提示信息
    :return: 用户输入内容，未输入则返回原有值
    """

    # 提示用户输入
    result_str  = input(tip_message)

    # 用户输入了内容，直接返回结果
    if len(result_str) > 0:

        return result_str

    # 用户没有输入内容，返回字典原有值
    else:

        return dict_value