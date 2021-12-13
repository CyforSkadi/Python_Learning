# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2021/12/13 0013 17:13

dan_ta = {"name":"蛋挞",
         "age":"21",
         "height":"183",
         "weight":"75"}

# 统计键值对数量
print(len(dan_ta))

# 合并字典 有相同key值会覆盖原有内容
temp_dict = {"gender":"male"}
dan_ta.update(temp_dict)

# 清空字典
dan_ta.clear()

print(dan_ta)