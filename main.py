import pygame
import Bird as B
import Load_pic as L
import Pipe as P
import sys
import os


def text(data, font_size, position, screen):
    font = pygame.font.Font('font.ttf', font_size)
    text = font.render(data, True, (0, 0, 0))
    text_width = text.get_width()
    text_height = text.get_height()
    screen.blit(text, (screen.get_width() // 2 - text_width // 2, screen.get_height() // position - text_height // 2))


def get_score(score, screen_w, bird, pipes):
    font_size = 40
    font = pygame.font.Font('font.ttf', font_size)
    score_text = font.render("{0}".format(score), True, (0, 0, 0))
    score_text_w = score_text.get_width()
    screen.blit(score_text, (screen_w - score_text_w - 5, 5))
    if pipes.cord[score][0] + bird.width <= bird.x:
        score += 1
    return score


if __name__ == '__main__':

    bird = None
    pipes = None
    frames = None
    score = None

    pygame.init()
    pygame.display.set_caption('Flappy')

    pygame.display.set_icon(pygame.image.load('bird_1.png'))

    background = L.load_pic('bg_1.png')
    screen_w = background.get_width()
    screen_h = background.get_height()
    screen = pygame.display.set_mode((screen_w, screen_h))

    running = True
    start = True
    jump_count = 0

    clock = pygame.time.Clock()

    while running:
        bird_flapped = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # křížek
                running = False
            elif event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:  # escape up
                running = False
            elif event.type == pygame.KEYDOWN and (
                    event.key == pygame.K_SPACE or event.key == pygame.K_UP) and not pipes.collision:
                bird_flapped = True
                start = False
            elif event.type == pygame.KEYUP and event.key == pygame.K_r and bird.land:
                start = True

        screen.blit(background, (0, 0))

        if start:
            score = 0
            frames = 1
            bird = B.Bird(screen, 'bird_1.png', 'bird_1_sit.png')
            pipes = P.Pipe('pipe.png')
            text("PRESS SPACE TO START", 40, 5, screen)

        else:
            pipes.generate(screen_w, screen_h)
            pipes.display_collision(screen, bird)

            frames = bird.movement(bird_flapped, screen_h, frames)

            pipes.movement(bird.land)

            if bird.land or pipes.collision:
                text("GAME OVER", 60, 3, screen)

            if bird.land:
                text("PRESS R TO RESTART", 30, 2, screen)

            score = get_score(score, screen_w, bird, pipes)

        screen.blit(bird.active, (bird.x, bird.y))
        pygame.display.flip()
        clock.tick(60)
        frames += 1

    pygame.quit()
