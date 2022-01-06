# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2022/1/5 0005 14:31
import pygame
from plane_sprites import *

# 游戏初始化
pygame.init()

# 创建游戏窗口 背景图480×700
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
# 加载图像数据
bg = pygame.image.load("./images/background.png")
# blit绘制图像
screen.blit(bg, (0, 0))
# pygame.display.update()

# 绘制英雄图像
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (150, 300))

# update更新屏幕显示
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

# 定义rect记录飞机初始位置
hero_rect = pygame.Rect(150, 300, 102, 126)

# 创建敌机精灵
enemy = GameSprite("./images/enemy1.png")
enemy1 = GameSprite("./images/enemy1.png", 2)
# 创建敌机精灵组
enemy_group = pygame.sprite.Group(enemy, enemy1)

# 游戏循环
while True:
    clock.tick(60)

    # 监听事件
    for event in pygame.event.get():
        # 判断是否退出
        if event.type == pygame.QUIT:
            print("游戏退出")
            pygame.quit()
            exit()
    # 修改飞机位置
    hero_rect.y -= 1
    # 判断飞机位置
    if hero_rect.y <= -126:
        hero_rect.y = 700
    # blit方法绘制图像
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    # 精灵族调用两个方法
    enemy_group.update()
    enemy_group.draw(screen)

    # 更新显示
    pygame.display.update()


