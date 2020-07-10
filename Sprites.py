import pygame
import spirtesheet

sl = spritesheet.spritesheet('sprites/ShopLeft.png')
sr = spritesheet.spritesheet('sprites/ShopRight.png')
sf = spritesheet.spritesheet('sprites/ShopFront.png')
sb = spritesheet.spritesheet('sprites/ShopBack.png')

class Player():
    def __init__(self, facing, x, y, image):
        self.facing = facing
        self.X = x
        self.Y = y
        self.load_images()
        self.image = image
        self.current_frame = 0
        self.last_update = 0
        self.rect
