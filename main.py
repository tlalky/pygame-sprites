import pygame
import random
import sys


class Crosshair(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("crosshair_outline_large.png")
        self.rect = self.image.get_rect()
        self.gunshot = pygame.mixer.Sound("Realistic-Gunshot-Sound-Effect.wav")  # add sound

    def shoot(self):
        self.gunshot.play()
        pygame.sprite.spritecollide(crosshair, target_group, True)

    def update(self):
        self.rect.center = pygame.mouse.get_pos()  # give x and y coordinates of mouse


class Target(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load("target_red1.png")
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)


pygame.init()
clock = pygame.time.Clock()

screen_size = screen_width, screen_height = (1400, 800)
screen = pygame.display.set_mode(screen_size)

background = pygame.image.load("bg.png")

pygame.mouse.set_visible(False)

crosshair = Crosshair()
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

target_group = pygame.sprite.Group()
for target in range(20):
    new_target = Target(random.randrange(0, screen_width), random.randrange(0, screen_height))
    target_group.add(new_target)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            crosshair.shoot()

    pygame.display.flip()
    screen.blit(background, (0, 0))
    target_group.draw(screen)
    crosshair_group.draw(screen)
    crosshair_group.update()
    clock.tick(60)




