import pygame

# Variables
SIZE = (1280, 720)
BACKGROUND_PICTURE = 'ressources/images/background.png'

pygame.init()  # initialise l'instance du jeu
screen = pygame.display.set_mode(SIZE)  # taille de l'ecran
# mise en place du background
background = pygame.image.load(BACKGROUND_PICTURE)

running = True
while running:

    screen.blit(background, (0, 0))

    pygame.display.flip()  # repeind l'ecran
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
