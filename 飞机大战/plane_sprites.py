# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2022/1/5 0005 14:44
import random
import pygame

# 屏幕大小常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 刷新帧率
FRAME_PER_SEC = 60
# 创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 英雄发射子弹定时器常量
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
    """
    飞机大战游戏精灵
    """
    def __init__(self, image_name, speed=1):
        # 调用父类初始化方法
        super().__init__()
        # 定义对象属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        # 在屏幕垂直方向上移动
        self.rect.y += self.speed


class BackGround(GameSprite):
    """
    游戏背景精灵
    """
    def __init__(self, is_alt=False):
        # 调用父类方法实现精灵创建
        super().__init__("./images/background.png")
        # 判断是否是交替图像，是则需要设置初始位置
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        # 调用父类方法实现移动
        super().update()
        # 判断是否移出屏幕，移出则将图像设置到屏幕上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.y


class Enemy(GameSprite):
    """
    敌机精灵
    """
    def __init__(self):
        # 调用父类方法创建敌机精灵，指定敌机图片
        super().__init__("./images/enemy1.png")
        # 指定敌机随机速度 1~3
        self.speed = random.randint(1, 3)
        # 指定敌机初始随机位置
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        # 调用父类方法，保持垂直飞行
        super().update()
        # 判断是否飞出屏幕，是则删除精灵
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()

    def __del__(self):
        pass


class Hero(GameSprite):
    """
    英雄精灵
    """
    def __init__(self):
        # 调用父类方法设置图像和速度
        super().__init__("./images/me1.png", 0)
        # 设置初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        # 创建子弹精灵组
        self.bullets = pygame.sprite.Group()

    def update(self):
        # 控制英雄在屏幕内
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
        elif self.rect.top < SCREEN_RECT.top:
            self.rect.top = SCREEN_RECT.top
        elif self.rect.bottom > SCREEN_RECT.bottom:
            self.rect.bottom = SCREEN_RECT.bottom

    def fire(self):
        # 创建子弹精灵

        for i in (0, 1, 2):
            bullet = Bullet()
            # 设置精灵位置
            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx
            # 将精灵添加到精灵组
            self.bullets.add(bullet)


class Bullet(GameSprite):
    """
    子弹精灵
    """
    def __init__(self):
        # 调用父类方法设置图像和速度
        super().__init__("./images/bullet1.png", -2)

    def update(self):
        # 调用父类方法使得子弹垂直飞行
        super().update()
        # 判断子弹是否飞出屏幕，飞出则删除
        if self.rect.bottom < 0:
            self.kill()

