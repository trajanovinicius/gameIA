import math

import pygame, sys

pygame.init()

size = width, height = 320*3, 240*3
speed = [0, 0]
black = 0, 0, 0

factor = .5
car_scale = (92*factor, 198*factor)

screen = pygame.display.set_mode(size)
car = pygame.image.load("carroca.png")
car = pygame.transform.scale(car, car_scale)
car_rect = car.get_rect()


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

    rot_car = pygame.transform.rotate(car, math.degrees(math.atan2(speed[0], speed[1])))

    # if car_rect.left < 0 or car_rect.right > width:
    #     speed[0] = -speed[0]
    #
    # if car_rect.top < 0 or car_rect.bottom > height:
    #     speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(rot_car, car_rect)
    pygame.display.flip()