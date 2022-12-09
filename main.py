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

        if (event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_a or event.key == pygame.K_LEFT):
                if(playerx >20):
                   playerx -= 20
                

            if(event.key == pygame.K_d or event.key == pygame.K_RIGHT):
                if (playerx < 930):
                    playerx += 20

            if(event.key == pygame.K_w or event.key == pygame.K_UP):
                if(playery > 20):
                    playery -= 20
                    

            if(event.key == pygame.K_s or event.key == pygame.K_DOWN):
                    if (playery < 775):
                        playery += 20

    player()
    pygame.display.update()