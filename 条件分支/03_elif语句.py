# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2021/12/12 0012 19:42

# 1. 定义 `holiday_name` 字符串变量记录节日名称
# 2. 如果是 **情人节** 应该 **买玫瑰**／**看电影**
# 3. 如果是 **平安夜** 应该 **买苹果**／**吃大餐**
# 4. 如果是 **生日** 应该 **买蛋糕**
# 5. 其他的日子每天都是节日啊……

holiday_name = "生日"

if holiday_name == "情人节":
    print("买玫瑰")
    print("看电影")
elif holiday_name == "平安夜":
    print("买苹果")
    print("吃大餐")
elif holiday_name == "生日":
    print("吃蛋糕")
else:
    print("每天都是节日啊")
