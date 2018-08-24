import pygame

class rey(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('/home/melman/Escritorio/rsz_melma_puntito.png')
        self.rect = self.image.get_rect()
        self.rect.center = (0, 300)

