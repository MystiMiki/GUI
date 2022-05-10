import pygame

if __name__ == '__main__':
    pygame.init()

    icon = pygame.image.load('icon.png')
    pygame.display.set_icon(icon)
    pygame.display.set_caption('PYGAME')

    running = True

    height = width = 700
    x = y = 200
    h_r = w_r = 100

    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((height, width))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # křížek
                running = False
            if event.type == pygame.KEYUP and event.key == pygame.K_UP and y > h_r:
                y -= 5
            if event.type == pygame.KEYUP and event.key == pygame.K_DOWN and y < height - h_r:  # Dolů
                y += 5
            if event.type == pygame.KEYUP and event.key == pygame.K_LEFT and x > w_r:  # Doleva
                x -= 5
            if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT and x < width - w_r:  # Doprava
                x += 5

        screen.fill((0, 0, 0))

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w] and y > 0:  # Nahoru
            y -= 5
        if pressed[pygame.K_s] and y < height - h_r:  # Dolů
            y += 5
        if pressed[pygame.K_a] and x > 0:  # Doleva
            x -= 5
        if pressed[pygame.K_d] and x < width - w_r:  # Doprava
            x += 5

        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(x, y, h_r, w_r), 10)
        pygame.display.flip()
        clock.tick(60)

