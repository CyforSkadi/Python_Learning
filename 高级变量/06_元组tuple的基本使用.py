# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2021/12/13 0013 16:35

# 元组中数据类型可以不同，一旦定义则不能修改
# 元组的定义
info_tuple = ("蛋挞", 21, 183)

# 索引
print(info_tuple[1])

# 计数
print("183出现了%d次" % info_tuple.count(183))

# 取索引
print(info_tuple.index("蛋挞"))

# 统计元组元素个数
print(len(info_tuple))
