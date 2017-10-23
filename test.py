#!/usr/bin/env python3

import pygame
from random import *
from pygame.locals import *


pygame.mixer.init()
pygame.mixer.music.load("./assets/John.wav")
pygame.mixer.music.play()

pygame.init()

fenetre = pygame.display.set_mode((700,400))

background = pygame.image.load("./assets/fond1.png").convert()
raquette1 = pygame.image.load("./assets/bat2.png").convert()
raquette2 = pygame.image.load("./assets/bat3.png").convert()
balle = pygame.image.load("./assets/ball2.png").convert()

rand = int(random() * 400)
pos_balle = balle.get_rect(topleft =(15, rand))
pos_raquette1 = raquette1.get_rect(topleft =(10, 150))
pos_raquette2 = raquette2.get_rect(topleft =(680, 150))
xr1 = 150
yr1 = 250
xr2 = 150
yr2 = 250
xb = 15
yb = rand
test = 0
test2 = 0
v = 250
compteur = 1

pygame.display.flip()

continuer = 1
clock = pygame.time.Clock()

def my_display() :    
        fenetre.blit(background, (0,0))
        fenetre.blit(balle, (pos_balle))
        fenetre.blit(raquette1, (pos_raquette1))
        fenetre.blit(raquette2, (pos_raquette2))
        pygame.display.flip()

my_display()


while continuer :
        for event in pygame.event.get():
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE : 
                        continuer = 0
        k = pygame.key.get_pressed()
        if k[K_DOWN] and pos_raquette2 != (680, 300, 10, 100):
                pos_raquette2 = pos_raquette2.move(0, 1)
                xr2 = xr2 + 1
                yr2 = yr2 + 1
        if k[K_UP] and pos_raquette2 != (680, 0, 10, 100):
                pos_raquette2 = pos_raquette2.move(0, -1)
                xr2 = xr2 - 1
                yr2 = yr2 - 1
        if k[K_z] and pos_raquette1 != (10, 0, 10, 100):
                pos_raquette1 = pos_raquette1.move(0, -1)
                xr1 = xr1 - 1
                yr1 = yr1 - 1
        if k[K_s] and pos_raquette1 != (10, 300, 10, 100):
                pos_raquette1 = pos_raquette1.move(0, 1)
                xr1 = xr1 + 1
                yr1 = yr1 + 1
        if xb == 673 and xr2 <= yb and yb <= yr2:
                test = 1
                compteur = compteur + 1
        if xb == 20 and xr1 <= yb and yb <= yr1:
                test = 0
        if yb == 390:
                test2 = 1
        if yb == 0:
                test2 = 0
        if xb == 693 or xb == 0:
                exit(82)
        if test == 1 and test2 == 0:
                pos_balle = pos_balle.move(-1, 1)
                xb = xb - 1
                yb = yb + 1
        elif test == 0 and test2 == 0:
                pos_balle = pos_balle.move(1, 1)
                xb = xb + 1
                yb = yb + 1
        elif test == 1 and test2 == 1:
                pos_balle = pos_balle.move(-1, -1)
                xb = xb - 1
                yb = yb - 1
        elif test == 0 and test2 == 1:
                pos_balle = pos_balle.move(1, -1)
                xb = xb + 1
                yb = yb - 1
        if compteur % 3 == 0:
                compteur = 1
                v = v + 40
        my_display()
        clock.tick(v)
