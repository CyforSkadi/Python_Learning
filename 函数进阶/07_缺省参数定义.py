# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2021/12/15 0015 20:04

# 必须保证带有默认值的缺省参数在参数列表末尾
def print_gender(name, title = "", gender = True):
    """
    打印性别
    :param title: 职位
    :param name: 姓名
    :param gender: True男生，False女生
    :return:
    """
    gender_text = "男生"

    if not gender:
        gender_text = "女生"

    print("[%s]%s 是 %s " % (title, name, gender_text))

# 在调用函数时，如果有多个缺省参数，需要指定参数名，这样解释器才能够知道参数的对应关系
print_gender("蛋挞", title="diemi")
print_gender("璇砸", gender=False)
