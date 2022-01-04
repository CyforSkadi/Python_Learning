# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2022/1/4 0004 14:17

file_read = open("README")
file_write = open("README[附件]", "w")

text = file_read.read()
file_write.write(text)

file_read.close()
file_write.close()
