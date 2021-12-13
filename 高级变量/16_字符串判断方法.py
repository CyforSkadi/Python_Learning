# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2021/12/13 0013 19:30

# 判断空白字符
space_str = "   \t"
print(space_str.isspace())

# 判断数字 不能判断小数
num_str = "\u00b2"
# 可以判断unicode字符串
print(num_str.isdigit())
# 只能判断单纯数字，但一般开发中使用这种
print(num_str.isdecimal())
# 可以判断中文数字
print(num_str.isnumeric())