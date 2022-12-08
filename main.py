import pygame

pygame.init()

screen = pygame.display.set_mode((1000,850))
pygame.display.set_caption("Alien Smasher")

playerimg = pygame.image.load("images/spaceship.png")
playerx = 470
playery = 750

def player():
    screen.blit(playerimg,(playerx,playery))

gameon = True

while gameon:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            gameon = False
    player()
    pygame.display.update()