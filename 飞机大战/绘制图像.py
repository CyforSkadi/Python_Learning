# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2022/1/5 0005 13:50
import pygame

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
screen.blit(hero, (200, 500))

# update更新屏幕显示
pygame.display.update()

while True:
    pass

pygame.quit()
