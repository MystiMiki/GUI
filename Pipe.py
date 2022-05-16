import Load_pic as L
import pygame
import random

RESCALE = 0.4
DISMOUNTING = 50
SPREAD_VELOCITY = 5
SPACE = 100


class Pipe:
    def __init__(self, img, move=1):
        self.bottom = L.load_pic(img, RESCALE)
        self.width = self.bottom.get_rect()[2]
        self.height = self.bottom.get_rect()[3]
        self.top = pygame.transform.flip(self.bottom, False, True)

        self.move = -move

        self.last = None
        self.collision = False

        self.cord = []

    def set_last(self):
        self.last = len(self.cord) - 1

    def generate(self, screen_w, screen_h):
        self.set_last()
        if len(self.cord) == 0 or screen_w - self.cord[self.last][0] == self.width * 3:
            start_y = screen_h // 2 + DISMOUNTING    # střed obrazovky + lehké sesazení dolu
            spread = random.randint(screen_h // -SPREAD_VELOCITY, screen_h // SPREAD_VELOCITY)  # rozmezí posunu trubek, 1/5 obrazovky
            y = start_y + spread
            self.cord.append([screen_w, y])

    def display_collision(self, screen, bird):
        for p in self.cord:
            # získání obdelníku pro kolize
            bird_rec = pygame.Rect(bird.x, bird.y, bird.width, bird.height)
            # zmenšení width a height o 1 pro lepší obrys
            bot_rec = pygame.Rect(p[0], p[1], self.width - 1, self.height - 1)
            top_rec = pygame.Rect(p[0], p[1] - self.height - SPACE, self.width - 1, self.height - 1)
            # p[1] - self.high ... posazení top trubky na bot trubku

            # vykreslení
            screen.blit(self.bottom, (bot_rec[0], bot_rec[1]))
            screen.blit(self.top, (top_rec[0], top_rec[1]))

            # ohraničení
            #pygame.draw.rect(screen, (0, 0, 0), bird_rec, 2, 20)
            #pygame.draw.rect(screen, (0, 0, 0), bot_rec, 2)
            #pygame.draw.rect(screen, (0, 0, 0), top_rec, 2)

            # kontrola kolize
            if bird_rec.colliderect(bot_rec) or bird_rec.colliderect(top_rec):
                self.collision = True

    def movement(self, land):
        if not self.collision and not land:
            for p in self.cord:
                p[0] += self.move
