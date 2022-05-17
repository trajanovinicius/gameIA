import math
import time
import random

import pygame
import sys

pygame.init()
clock = pygame.time.Clock()

size = width, height = 320*3, 240*3
speed = [0, 0]
black = 0, 0, 0

factor = 0.2
car_scale = (92*factor, 198*factor)

screen = pygame.display.set_mode(size)

car = pygame.image.load("img/carro2.png")
car = pygame.transform.scale(car, car_scale)
car_rect = car.get_rect()
car_rect = car_rect.move(size[0]/2, 70)


tree = pygame.image.load('img/tree.png')
rect_trees = []
for i in range(16):

    rect_trees.append(tree.get_rect())
    tree = pygame.transform.scale(tree, (100, 100))
    rect_trees[i] = rect_trees[i].move(
        random.random() * size[0], size[1] * random.random())

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed[0] += -1
            if event.key == pygame.K_RIGHT:
                speed[0] += +1
            if event.key == pygame.K_UP:
                speed[1] += -1
            if event.key == pygame.K_DOWN:
                speed[1] += +1

    car_rect = car_rect.move(speed)
    if car_rect.left < 0 or car_rect.right > size[0] or car_rect.top < 0 or car_rect.bottom > size[1]:
        car_rect = car_rect.move((-speed[0], -speed[1]))
        speed = [0, 0]

    rot_car = pygame.transform.rotate(
        car, math.degrees(math.atan2(speed[0], speed[1])))

    screen.fill((170, 255, 160))

    # TODO: remove those magic numbers
    pygame.draw.ellipse(screen, (128, 128, 128), (30, 30, 900, 660))
    pygame.draw.ellipse(screen, (170, 255, 160), (130, 130, 700, 460))
    mid = size[0]/2
    pygame.draw.line(screen, 'white', (mid, 31), (mid, 130), 3)

    screen.blit(rot_car, car_rect)
    pygame.draw.line(screen, 'red', car_rect.center,
                     (car_rect.center[0] + speed[0]*400, car_rect.center[1] + speed[1] * 400))

    for i in range(16):
        screen.blit(tree, rect_trees[i])

    pygame.display.flip()
    clock.tick(60)
