# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2022/1/4 0004 14:21

file_read = open("README")
file_write = open("README[附件]", "w")

while True:
    text = file_read.readline()

    if not text:
        break

    file_write.write(text)

file_read.close()
file_write.close()
