import Load_pic as L
import pygame
import random

rescale = 0.4


class Pipe:
    def __init__(self, img, move=1):
        self.bottom, self.width, self.height = L.load_pic(img, rescale)
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
            y = 50 + random.randint(screen_h // -5, screen_h // 5) + screen_h // 2
            self.cord.append([screen_w, y])

    def display_collision(self, screen, bird):
        for p in self.cord:
            screen.blit(self.bottom, (p[0], p[1]))
            screen.blit(self.top, (p[0], -self.height - 100 + p[1]))
            bird_rec = pygame.Rect(bird.x, bird.y, bird.width, bird.height)
            bot_rec = pygame.Rect(p[0], p[1], self.width - 1, self.height - 1)
            top_rec = pygame.Rect(p[0], -self.height - 100 + p[1], self.width - 1, self.height - 1)

            # ohraničení
            # pygame.draw.rect(screen, (0, 0, 0), bird_rec, 2, 20)
            # pygame.draw.rect(screen, (0, 0, 0), pipe_rec, 2)
            # pygame.draw.rect(screen, (0, 0, 0), top_pipe_rec, 2)

            if bird_rec.colliderect(bot_rec) or bird_rec.colliderect(top_rec):
                self.collision = True

    def movement(self, land):
        if not self.collision and not land:
            for p in self.cord:
                p[0] += self.move
