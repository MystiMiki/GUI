## Skóre

1. Vytvoříme *get_score* v *main.py*
   
   Jak můžeme získávat skóre? Kdy se nám přičte bod? Můžeme využít něco z předchozích tříd?
   
   <details>
   <summary>get_score</summary>

   ```python
   def get_score(score, screen_w, bird, pipes):
       font_size = 40
       font = pygame.font.Font('font.ttf', font_size)
       score_text = font.render("{0}".format(score), True, (0, 0, 0))
       score_text_w = score_text.get_width()
       screen.blit(score_text, (screen_w - score_text_w - 5, 5))
       if pipes.cord[score][0] + bird.width <= bird.x:
           score += 1
       return score
   ```
   </details>  
