# Python 基础学习
# 蛋挞不能吃
# 学习时间： 2022/1/5 0005 13:36

import pygame

hero_rect = pygame.Rect(100, 500, 120, 125)

print("英雄的原点: %d %d" % (hero_rect.x, hero_rect.y))
print("英雄的尺寸: %d %d" % (hero_rect.width, hero_rect.height))
print("%d %d" % hero_rect.size)
