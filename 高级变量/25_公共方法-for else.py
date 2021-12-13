# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2021/12/13 0013 20:30

# for 变量 in 集合:
#     循环体代码
# else:
#     没有通过break退出循环，循环结束后，会执行的代码

for num in [1, 2, 3]:

    print(num)

    if num == 2:
        break

else:
    print("会执行嘛")

print("循环结束")

# 应用场景
# 需求：要判断某一个字典中是否存在指定的值
# 如果存在，提示并且退出循环
# 如果不存在，在循环整体结束后，希望得到一个统一的提示
student = [
    {"name":"蛋挞"},
    {"name":"璇砸"}
]

find_name = "蛋挞"

for stu in student:

    if stu["name"] == find_name:
        print("找到了%s" % find_name)
        break
else:
    print("未找到目标")


print("循环结束")