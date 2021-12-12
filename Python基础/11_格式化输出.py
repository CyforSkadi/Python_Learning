# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2021/12/12 0012 17:33

"""
语法：
print("格式化字符串" % 变量1)
print("格式化字符串" % (变量1, 变量2...))

| %s   | 字符串                                                       |
| ---- | ------------------------------------------------------------ |
| %d   | 有符号十进制整数，`%06d` 表示输出的整数显示位数，不足的地方使用 `0` 补全 |
| %f   | 浮点数，`%.2f` 表示小数点后只显示两位                        |
| %%   | 输出 `%`                                                     |
"""

name = "蛋挞"
age = 21
print("我的名字叫%s,今年%d岁" % (name, age))

