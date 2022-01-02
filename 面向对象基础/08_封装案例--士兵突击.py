# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2022/1/2 0002 13:56

class Gun:

    def __init__(self, model):

        self.model = model
        self.bullet_count = 0

    def add_bullet(self, count):

        self.bullet_count += count

    def shoot(self):

        if self.bullet_count <= 0:
            print("[%s]没有子弹" % self.model)
            return

        self.bullet_count -= 1
        print("[%s]突突突  [%d]" % (self.model, self.bullet_count))


class Soldior:

    def __init__(self, name):

        self.name = name
        self.gun = None

    def fire(self):

        # is/is not 身份运算符 判断两个标识符是否引用同一个对象
        if self.gun is None:
            print("[%s]还没有枪" % self.name)
            return

        print("冲啊")
        self.gun.add_bullet(50)
        self.gun.shoot()


ak47 = Gun("AK47")

# ak47.add_bullet(50)
# ak47.shoot()

xusanduo = Soldior("许三多")
xusanduo.gun = ak47
xusanduo.fire()
print(xusanduo.gun)
