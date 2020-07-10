import pygame

# write words on the screen
white = (255, 255, 255)
screen = pygame.display.set_mode((256, 128))

class Phrase(object):
    def __init__(self, text, on, x, y, colour, size):
        self.text = text
        self.on = on
        self.X = x
        self.Y = y
        self.colour = colour
        self.size = size

    def write(self):
        my_font = pygame.font.Font("fonts/PokemonGB-RAeo.ttf", self.size)
        label = my_font.render(self.text, 1, self.colour)
        text = screen.blit(label, (self.X, self.Y))
        return text


P1 = Phrase("The chest opened!", False, 10, 116, white, 10)
P2 = Phrase("Hello world", False, 10, 116, white, 10)
P3 = Phrase("You found a red key!", False, 10, 116, white, 10)
P4 = Phrase("You found a blue key!", False, 10, 116, white, 10)
P5 = Phrase("You found a green key!", False, 10, 116, white, 10)
P6 = Phrase("You found a yellow key!", False, 10, 116, white, 10)
P7 = Phrase("The cardboard box opened!", False, 10, 116, white, 10)
P8 = Phrase("You played a record!", False, 10, 116, white, 10)
P9 = Phrase("You stopped the record!", False, 10, 116, white, 10)
P10 = Phrase("You have no items!", False, 10, 116, white, 10)
P11 = Phrase("Your phone is not charged!", False, 10, 116, white, 10)
P12 = Phrase("You're already dressed!", False, 10, 116, white, 10)
P13 = Phrase("Figure it out!", False, 10, 116, white, 10)

phrases = [P1, P2, P3, P4, P5, P6, P7, P8, P9, P10, P11, P12, P13]