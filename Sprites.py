import pygame
import room

all_sprites = pygame.sprites.Group()


class Player(pygame.sprite.Sprite):
    def __init__(self, filename):
        pygame.sprite.Sprite.__init__(self)
        self.sheet = pygame.image.load(filename).convert_alpha()

        # Load a specific image from a specific rectangle

        def image_at(self, rectangle):
            # "Loads image from x,y,x+offset,y+offset"
            rect = pygame.Rect(rectangle)
            image = pygame.Surface(rect.size).convert()
            image.blit(self.sheet, (0, 0), rect)
            colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
            return image