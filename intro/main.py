def set_moving_circle():
    pygame.display.set_caption('Moving circle')

    icon = pygame.image.load('circle.png')
    pygame.display.set_icon(icon)


def moving_circleA():
    screen = pygame.display.set_mode((800, 600))
    pygame.draw.circle(screen, (0, 0, 255), (400, 300), 150)


def moving_circleB():
    while True:
        screen = pygame.display.set_mode((800, 600))
        pygame.draw.circle(screen, (0, 0, 255), (400, 300), 150)
        pygame.display.flip()  # aktualizace obrazovky


def exit(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # křížek
            running = False
        elif event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:  # Escape up
            running = False
    return running


def moving_circleC():
    running = True

    while running:
        running = exit(running)
        screen = pygame.display.set_mode((800, 600))
        pygame.draw.circle(screen, (0, 0, 255), (400, 300), 150)
        pygame.display.flip()


def moving_circleD():
    running = True
    player_x = 400
    player_y = 300
    clock = pygame.time.Clock()  # vytvoříme nové pygame hodiny

    while running:
        running = exit(running)
        width = 800
        height = 600
        screen = pygame.display.set_mode((width, height))
        size = 100
        pygame.draw.circle(screen, (0, 0, 255), (player_x, player_y), size)
        pygame.display.flip()
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w] and player_y > size:  # Nahoru
            player_y -= 5
        if pressed[pygame.K_s] and player_y < height - size:  # Dolů
            player_y += 5
        if pressed[pygame.K_a] and player_x > size:  # Doleva
            player_x -= 5
        if pressed[pygame.K_d] and player_x < width - size:  # Doprava
            player_x += 5
        clock.tick(60)  # omezeni rychlosti


def set_flappy():
    pygame.display.set_caption('Flappy')

    icon = pygame.image.load('bird_1.png')
    pygame.display.set_icon(icon)


def background_text():
    running = True

    while running:
        running = exit(running)
        pygame.font.get_fonts()  # výpis fontů
        font_size = 20
        font = pygame.font.SysFont('comicsansms', font_size)

        background = pygame.image.load('bg_1.png')
        rect = background.get_rect()
        rescale = 1
        screen_width = rect[2] // rescale
        screen_height = rect[3] // rescale
        screen = pygame.display.set_mode((screen_width, screen_height))
        background = pygame.transform.scale(background, (screen_width, screen_height))
        screen.blit(background, (0, 0))

        text = font.render("PRESS SPACE TO START ", True, (0, 0, 0))
        text_width = text.get_width()
        text_height = text.get_height()

        screen.blit(text, (screen_width // 2 - text_width // 2, screen_height // 5 - text_height // 2))
        pygame.display.flip()


def load_pic(picture, rescale):
    bird = pygame.image.load(picture)
    rect = bird.get_rect()
    rescale_width = int(rect[2] * rescale)
    rescale_height = int(rect[3] * rescale)
    bird = pygame.transform.scale(bird, (rescale_width, rescale_height))
    return bird, rescale_width, rescale_height


def moving_bird():
    running = True
    start = True
    gravity = 1
    pipe_cord = []
    move = -1
    bird_velocity_y = 0
    bird_flap_velocity = -30
    clock = pygame.time.Clock()

    pygame.font.get_fonts()  # výpis fontů
    font_size = 40
    font = pygame.font.Font('font.ttf', font_size)
    text = font.render("PRESS SPACE TO START", True, (0, 0, 0))
    text_width = text.get_width()
    text_height = text.get_height()

    over = font.render("GAME OVER", True, (0, 0, 0))
    over_width = over.get_width()
    over_height = over.get_height()

    background = pygame.image.load('bg_1.png')

    pipe, pipe_width, pipe_height = load_pic('pipe.png', 0.4)
    top_pipe = pygame.transform.flip(pipe, False, True)
    score = 0
    game = True

    screen_width = background.get_width()
    screen_height = background.get_height()
    screen = pygame.display.set_mode((screen_width, screen_height))
    background = pygame.transform.scale(background, (screen_width, screen_height))

    bird, bird_width, bird_height = load_pic('bird_1.png', 1.5)
    bird_x = screen_width // 2 - bird_width // 2
    bird_y = screen_height // 2 - bird_height // 2

    while running:
        bird_flapped = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # křížek
                running = False
            elif event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:  # Escape up
                running = False
            elif event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_UP) and game:
                bird_velocity_y += bird_flap_velocity
                bird_flapped = True
                start = False

        screen.blit(background, (0, 0))
        if start:
            screen.blit(text, (screen_width // 2 - text_width // 2, screen_height // 5 - text_height // 2))

        else:
            # trubky - generování ... osa y
            last = len(pipe_cord) - 1
            if len(pipe_cord) == 0 or screen_width - pipe_cord[last][0] == pipe_width * 3:
                y = 50 + random.randint(screen_height // -5, screen_height // 5) + screen_height // 2
                pipe_cord.append([screen_width, y])

            # trubky - zobrazování
            for p in pipe_cord:
                screen.blit(pipe, (p[0], p[1]))
                screen.blit(top_pipe, (p[0], -pipe_height-100+p[1]))
                bird_rec = pygame.Rect(bird_x, bird_y, bird_width, bird_height)
                pipe_rec = pygame.Rect(p[0], p[1], pipe_width-1, pipe_height-1)
                top_pipe_rec = pygame.Rect(p[0], -pipe_height-100+p[1], pipe_width-1, pipe_height-1)

                # ohraničení
                #pygame.draw.rect(screen, (0, 0, 0), bird_rec, 2, 20)
                #pygame.draw.rect(screen, (0, 0, 0), pipe_rec, 2)
                #pygame.draw.rect(screen, (0, 0, 0), top_pipe_rec, 2)

                # trubky - kontrola kolize
                if bird_rec.colliderect(pipe_rec) or bird_rec.colliderect(top_pipe_rec):
                    game = False

            # trubky - pohyb ... osa x
            if game:
                for p in pipe_cord:
                    p[0] += move

            # pták - pohyb ... osa y
            if bird_flapped and (bird_y + bird_velocity_y) > 0:
                bird_y += bird_velocity_y
            elif bird_y <= (screen_height - bird_height):
                bird_y += gravity
            if bird_y >= (screen_height - bird_height):
                bird, bird_width, bird_height = load_pic('bird_1_sit.png', 1.5)
                game = False

            # kontrola konce hry
            if not game:
                screen.blit(over, (screen_width // 2 - over_width // 2, screen_height // 2 - over_height // 2))

            # skóre
            score_text = font.render("{0}".format(score), True, (0, 0, 0))
            score_text_w = score_text.get_width()
            score_text_h = score_text.get_height()
            screen.blit(score_text, (screen_width - score_text_w - 5, screen_height - screen_height + 5))
            if pipe_cord[score][0] + bird_width <= bird_x:
                score += 1

        screen.blit(bird, (bird_x, bird_y))
        bird_velocity_y = 0

        pygame.display.flip()
        clock.tick(60)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # zpětná kompatibilita se všemi verzemi pygame
    try:
        import pygame_sdl2  # tries to import pygame_sdl2

        pygame_sdl2.import_as_pygame()  # mask pygame_sdl2 as pygame
    except ImportError:
        pass

    import pygame

    import random

    pygame.init()

    #set_moving_circle()
    # Vytvoření okna, vykreslení kruhu
    # moving_circleA()

    # Okno zůstane na obrazovce
    # moving_circleB()

    # Okno lze zavřít křížkem
    # moving_circleC()

    # Pohyb
    #moving_circleD()

    set_flappy()
    # background a text
    # background_text()

    moving_bird()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
