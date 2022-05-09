## Ptáček

1. Vytvoříme si class *Bird.py*

   Co vše potřebujeme?
   <details>
   <summary>Bird.py</summary>

   ```python
   import Load_pic as L

   rescale = 1.5


   class Bird:
       def __init__(self, fly, sit, flap_velocity=2):
           self.fly, self.width, self.height = L.load_pic(fly, rescale)
           self.sit, _, _ = L.load_pic(sit, rescale)

           self.active = self.fly
           self.land = False

           self.x = None
           self.y = None

           self.gravitation = -1/20
           self.flap_velocity = -flap_velocity
           self.flapped = False
           self.vert_speed = 0

       def set_x(self, screen_w):
           self.x = screen_w // 2 - self.width // 2

       def set_y(self, screen_h):
           self.y = screen_h // 2 - self.height // 2
   ```
   </details>  
   
2. Pohyb
   <details>
   <summary>movement</summary>

   ```python
   def movement(self, bird_flapped, jump_count, screen_h, frames):
     if bird_flapped and self.y + jump_count * self.flap_velocity > 0: #začátek skoku
         self.vert_speed = self.flap_velocity
         frames = 0
     if self.y <= (screen_h - self.height):
         self.y += self.vert_speed * frames / 70
         self.vert_speed -= self.gravitation * frames / 70
     if self.y >= (screen_h - self.height): #přistání
         self.y = screen_h - self.height
         self.active = self.sit
         self.land = True

     return frames
   ```
   </details>  
