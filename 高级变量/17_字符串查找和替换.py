# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2021/12/13 0013 19:37

str = "hello Python"

# 判断是否以指定字符串开始
print(str.startswith("hello"))

# 判断是否以指定字符串结束
print(str.endswith("Python"))

# 查找对应字符串 返回索引位置，没找到返回-1
print(str.find("Py"))

# 替换字符串 replace执行完成后返回一个新字符串，不修改原字符串内容
print(str.replace("Python", "python"))
