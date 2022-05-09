## Kolize

Jelikož zobrazování i kolize děláme pro všechny trubky, můžeme provést oboje v jednom cyklu. Nejprve si trubky zobrazíme pomocí příkazu **blit**,
poté kontrolujeme kolize s ptáčkem.

1. Metoda display_collision 
   
   <details>
   <summary>Pipe.py</summary>

   ```python
   def display_collision(self, screen, bird):
       for p in self.cord:
           screen.blit(self.bottom, (p[0], p[1]))
           screen.blit(self.top, (p[0], -self.height - 100 + p[1]))
           bird_rec = pygame.Rect(bird.x, bird.y, bird.width, bird.height)
           bot_rec = pygame.Rect(p[0], p[1], self.width - 1, self.height - 1)
           top_rec = pygame.Rect(p[0], -self.height - 100 + p[1], self.width - 1, self.height - 1)

           if bird_rec.colliderect(bot_rec) or bird_rec.colliderect(top_rec):
               self.collision = True
   ```
   </details>  
   
2. Zobrazení ohraničení 

   Pomocí **draw.rect**, parametry (obrazovka, barva, obdelník, tlouštka, zaoblení)
    ```python
            pygame.draw.rect(screen, (0, 0, 0), bird_rec, 2, 20)
            pygame.draw.rect(screen, (0, 0, 0), pipe_rec, 2)
            pygame.draw.rect(screen, (0, 0, 0), top_pipe_rec, 2)
    ```
   
