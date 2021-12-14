# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2021/12/14 0014 16:42

# 不可变类型，内存中的数据不允许被修改：
# 数字类型 `int`, `bool`, `float`, `complex`, `long(2.x)`
# 字符串 `str`
# 元组 `tuple`
# 可变类型，内存中的数据可以被修改：
# 列表 `list`
# 字典 `dict`

demo_list = [1, 2, 3]

print("定义列表后的内存地址 %d" % id(demo_list))

demo_list.append(999)
demo_list.pop(0)
demo_list.remove(2)
demo_list[0] = 10

print("修改数据后的内存地址 %d" % id(demo_list))

demo_dict = {"name": "小明"}

print("定义字典后的内存地址 %d" % id(demo_dict))

demo_dict["age"] = 18
demo_dict.pop("name")
demo_dict["name"] = "老王"

print("修改数据后的内存地址 %d" % id(demo_dict))

# 字典中key只能是不可变类型变量

# * `Python` 中内置有一个名字叫做 `hash(o)` 的函数
#   * 接收一个 **不可变类型** 的数据作为 **参数**
#   * **返回** 结果是一个 **整数**
# * `哈希` 是一种 **算法**，其作用就是提取数据的 **特征码（指纹）**
#   * **相同的内容** 得到 **相同的结果**
#   * **不同的内容** 得到 **不同的结果**
hash(1)

print(hash("hello"))
print(hash("hello"))

print(hash("hello1"))

# 列表和字典不能哈希
# print(hash([]))
