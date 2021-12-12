# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2021/12/12 0012 19:48

# 1. 定义布尔型变量 `has_ticket` 表示是否有车票
# 2. 定义整型变量 `knife_length` 表示刀的长度，单位：厘米
# 3. 首先检查是否有车票，如果有，才允许进行 **安检**
# 4. 安检时，需要检查刀的长度，判断是否超过 20 厘米
#    * 如果超过 20 厘米，提示刀的长度，不允许上车
#    * 如果不超过 20 厘米，安检通过
# 5. 如果没有车票，不允许进门

has_ticket = True
knife_length = 15

if has_ticket:
    print("允许进行安检")
    if knife_length > 20:
        print("您携带的刀具长为%dcm,不允许上车" % knife_length)
    else:
        print("安检通过,祝您旅途愉快")
else:
    print("请先买票")
