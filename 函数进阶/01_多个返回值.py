# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2021/12/15 0015 19:29

def measure():
    """
    测量温度和湿度
    :return:
    """
    print("测量开始")
    temp = 39
    wetness = 50
    print("测量结束")

    # 使用元组让函数返回多个值,()可以省略
    return temp, wetness


result = measure()
print(result)

# 如果函数返回元组且希望单独处理元组中的元素
# 可以使用多个变量一次接受函数返回值
gl_temp, gl_wetness = measure()

print(gl_temp)
print(gl_wetness)
