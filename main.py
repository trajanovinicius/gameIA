import math
import pygame
import sys

pygame.init()
clock = pygame.time.Clock()

size = width, height = 320*4, 240*4
speed = [0, 0]
black = 0, 0, 0

car_scale = (92, 198)  # escala da imagem do carro

screen = pygame.display.set_mode(size)
car = pygame.image.load("carro2.png")  # utilizando a imagem do carro
car = pygame.transform.scale(car, car_scale)
car_rect = car.get_rect()


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:  # Criando movimentação do carro pelo teclado
            if event.key == pygame.K_LEFT:
                speed[0] += -1
            if event.key == pygame.K_RIGHT:
                speed[0] += 1
            if event.key == pygame.K_UP:
                speed[1] += -1
            if event.key == pygame.K_DOWN:
                speed[1] += +1

    car_rect = car_rect.move(speed)
    rot_car = pygame.transform.rotate(
        car, math.degrees(math.atan2(speed[0], speed[1])))

    screen.fill(black)
    screen.blit(rot_car, car_rect)
    pygame.display.flip()
    clock.tick(10)
