# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2021/12/13 0013 15:51

# 列表的定义
name_list = ["蛋挞", "璇砸"]

# 列表中的方法
# | 序号 | 分类 | 关键字 / 函数 / 方法    | 说明                     |
# | 1    | 增加 | 列表.insert(索引, 数据) | 在指定位置插入数据       |
# |      |      | 列表.append(数据)       | 在末尾追加数据           |
# |      |      | 列表.extend(列表2)      | 将列表2 的数据追加到列表 |
# | 2    | 修改 | 列表[索引] = 数据       | 修改指定索引的数据       |
# | 3    | 删除 | del 列表[索引]          | 删除指定索引的数据       |
# |      |      | 列表.remove[数据]       | 删除第一个出现的指定数据 |
# |      |      | 列表.pop                | 删除末尾数据             |
# |      |      | 列表.pop(索引)          | 删除指定索引数据         |
# |      |      | 列表.clear              | 清空列表                 |
# | 4    | 统计 | len(列表)               | 列表长度                 |
# |      |      | 列表.count(数据)        | 数据在列表中出现的次数   |
# | 5    | 排序 | 列表.sort()             | 升序排序                 |
# |      |      | 列表.sort(reverse=True) | 降序排序                 |
# |      |      | 列表.reverse()          | 逆序、反转               |

# 列表索引[]，从0开始
print(name_list[0])
print(name_list[1])

# 取索引
print(name_list.index("蛋挞"))

# 修改
name_list[0] = "蛋挞不能吃"
print(name_list)

# 增加数据(append, insert, extend)
name_list.append("棉棉")

name_list.insert(1,"蛋挞")

temp_list = ["哈", "哈哈"]
name_list.extend(temp_list)

print(name_list)

# 删除数据(clear, remove, pop)
name_list.remove("蛋挞不能吃")

name_list.pop()
name_list.pop(3)

name_list.clear()

print(name_list)