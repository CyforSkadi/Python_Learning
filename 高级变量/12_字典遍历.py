# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2021/12/13 0013 17:16

dan_ta = {"name":"蛋挞",
         "age":"21",
         "height":"183",
         "weight":"75"}

# 迭代遍历字典
# 变量k是每次循环中获取键值对的key值
for k in dan_ta:

    print("%s - %s" % (k, dan_ta[k]))
