import pygame
import sys
import carro_enemigo
from pygame.locals import *
import random
import json
from datetime import datetime

Clock = pygame.time.Clock()


background_image = pygame.image.load("Imagenes/Menu_inicio.jpg")

size = width, height = 800, 500

def main():
    pygame.init()
    screen = pygame.display.set_mode((800,500))
    background_image = pygame.image.load("Imagenes/Menu_inicio.jpg")
    background_rect = background_image.get_rect()
    running = True

    while running:
        screen.blit(background_image, background_rect)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
    
    pygame.quit()
    sys.exit()


