## Trubky

1. Vytvoříme si class *Pipe.py*

   Co vše potřebujeme?
   
   Z classy *bird.py* víme, že budeme opět načítat obrázek trubky. Trubku máme ze zhora i spoda. Lze použít pouze jeden obrázek, 
   který bude upravený pomocí nějaké metody v pygame?
   
   <details>
   <summary>Pipe.py</summary>

   ```python
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
   ```
   </details>  
   
2. Pohyb
   <details>
   <summary>movement</summary>

   ```python
   def movement(self, land):
       if not self.collision and not land:
            for p in self.cord:
                p[0] += self.move
   ```
   </details>  
   
