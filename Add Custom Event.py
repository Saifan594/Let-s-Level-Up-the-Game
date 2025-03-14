print("\033c")

import random
import pygame

pygame.init()

display_size = (750, 500)
display_image = pygame.transform.scale(pygame.image.load("display image.jpg"), display_size)
display = pygame.display.set_mode(display_size)

font = pygame.font.SysFont("timesnewroman", 100)
font_surface = font.render("You Win!", True, pygame.Color("black"))

all_sprites = pygame.sprite.Group()

score = 0
running = True
win = False
clock = pygame.time.Clock()

class Sprite(pygame.sprite.Sprite):
    def __init__(self, width, height, color):
        super().__init__()
        
        self.image = pygame.Surface((width, height))
        
        self.image.fill(pygame.Color("blue"))
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))
        
        self.rect = self.image.get_rect()
    
    def move(self, x_velocity, y_velocity):
        self.rect.x = max(min(self.rect.x + x_velocity, display_size[0] - self.rect.width), 0)
        self.rect.y = max(min(self.rect.y + y_velocity, display_size[1] - self.rect.height), 0)

snake = Sprite(50, 50, pygame.Color("green"))
snake.rect.x = (display_size[0] - snake.rect.width) / 2
snake.rect.y = (display_size[1] - snake.rect.height) / 2
all_sprites.add(snake)

food = Sprite(25, 25, pygame.Color("red"))
food.rect.x = random.randint(0, display_size[0] - food.rect.width)
food.rect.y = random.randint(0, display_size[1] - food.rect.height)
all_sprites.add(food)

pygame.display.set_caption("Add Custom Event")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if not win:
        key = pygame.key.get_pressed()
        
        x_velocity = (key[pygame.K_RIGHT] - key[pygame.K_LEFT]) * 5
        y_velocity = (key[pygame.K_DOWN] - key[pygame.K_UP]) * 5
        
        snake.move(x_velocity, y_velocity)
        
        if snake.rect.colliderect(food.rect):
            all_sprites.remove(food)
            score += 1
            
            if score == 5:
                win = True
            
            else:
                food.rect.x = random.randint(0, display_size[0] - food.rect.width)
                food.rect.y = random.randint(0, display_size[1] - food.rect.height)
                all_sprites.add(food)
    
    display.blit(display_image, (0, 0))
    all_sprites.draw(display)
    
    if win:
        display.blit(font_surface, ((display_size[0] - font_surface.get_width()) / 2, (display_size[1] - font_surface.get_height()) / 2))
    
    pygame.display.flip()
    clock.tick(100)

pygame.quit()