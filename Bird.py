import Load_pic as L

RESCALE = 1.5
G_ACCELERATION = 1/20
LEVEL = 70


class Bird:
    def __init__(self, screen, fly, sit, flap_velocity=2):
        self.fly = L.load_pic(fly, RESCALE)
        self.sit = L.load_pic(sit, RESCALE)
        self.width = self.fly.get_rect()[2]
        self.height = self.fly.get_rect()[3]

        self.active = self.fly  # aktivní obrázek
        self.land = False   # zda přistál ... False = letí

        self.x = screen.get_rect()[2] // 2 - self.width // 2
        self.y = screen.get_rect()[3] // 2 - self.height // 2

        self.gravitation = G_ACCELERATION
        self.flap_velocity = -flap_velocity
        self.flapped = False    # zda vzletěl ... False = nevzletěl
        self.vert_speed = 0

    def movement(self, bird_flapped, screen_h, frames):
        if not self.land:   # pokud letí
            if bird_flapped and self.y + self.flap_velocity > 0:   # začátek skoku, horní hranice
                self.vert_speed = self.flap_velocity    # počátěční nastavení vertikální rychlosti pro posun nahoru
                frames = 0  # vynulování pro výpočet gravitačního zrychlení při padání
            if self.y <= (screen_h - self.height): # dolní hranice
                self.y += self.vert_speed * frames / LEVEL  # rovnice ... čas = frames / LEVEL
                self.vert_speed += self.gravitation * frames / LEVEL    # přepočet vertikální rychlosti ze stoupání na klesání
            if self.y >= (screen_h - self.height):  # pokud pod dolní hranicí => přistání
                self.y = screen_h - self.height
                self.active = self.sit
                self.land = True

        return frames


