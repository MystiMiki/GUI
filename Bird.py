import Load_pic as L

rescale = 1.5


class Bird:
    def __init__(self, fly, sit, move=1, flap_velocity=30):
        self.fly, self.width, self.height = L.load_pic(fly, rescale)
        self.sit, _, _ = L.load_pic(sit, rescale)

        self.active = self.fly
        self.land = False

        self.x = None
        self.y = None

        self.gravitation = 1
        self.move = -move
        self.flap_velocity = -flap_velocity
        self.flapped = False

    def set_x(self, screen_w):
        self.x = screen_w // 2 - self.width // 2

    def set_y(self, screen_h):
        self.y = screen_h // 2 - self.height // 2

    def movement(self, bird_flapped, jump_count, screen_h, frames):
        if bird_flapped and (x := (self.y + jump_count * self.flap_velocity)) > 0:
            self.y = x
            frames = 0
        elif self.y <= (screen_h - self.height):
            #self.y += 1
            self.y += 1/10 * self.gravitation * frames
        if self.y >= (screen_h - self.height):
            self.y = screen_h - self.height
            self.active = self.sit
            self.land = True
        return frames


