# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2021/12/12 0012 19:29

# 练习1: 定义一个整数变量 `age`，编写代码判断年龄是否正确
# 要求人的年龄在 0-120 之间
# age = int(input("请输入年龄："))
#
# if age <= 120 and age >= 0 :
#     print("年龄正确")
# else:
#     print("年龄不正确")

# 练习2: 定义两个整数变量 `python_score`、`c_score`，编写代码判断成绩
# 要求只要有一门成绩 > 60 分就算合格
# python_score = 75
# c_score = 55
#
# if python_score > 60 or c_score >60:
#     print("考试通过")
# else:
#     print("考试失败")

# 练习3: 定义一个布尔型变量 `is_employee`，编写代码判断是否是本公司员工
# 如果不是提示不允许入内
is_employee = True

if not is_employee:
    print("不允许入内")
else:
    print("允许入内")