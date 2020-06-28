import pygame
import spritesheet
from pygame import mixer

# initialize pygame
pygame.init()

pygame.display.set_caption('Room')
clock = pygame.time.Clock()

# create screen
screen = pygame.display.set_mode((256, 128))

black = (0, 0, 0)
white = (255, 255, 255)

# Player Image
sl = spritesheet.spritesheet('sprites/ShopLeft.png')
sr = spritesheet.spritesheet('sprites/ShopRight.png')
sf = spritesheet.spritesheet('sprites/ShopFront.png')
sb = spritesheet.spritesheet('sprites/ShopBack.png')

# left walk image list
sl1 = sl.image_at((0, 0, 19, 30))
sl2 = sl.image_at((20, 0, 19, 30))
sl3 = sl.image_at((40, 0, 19, 30))
sl4 = sl.image_at((40, 0, 19, 30))

walk_left = [sl1, sl2, sl3, sl4]

# left walk image list
sr1 = sr.image_at((0, 0, 19, 30))
sr2 = sr.image_at((20, 0, 19, 30))
sr3 = sr.image_at((40, 0, 19, 30))
sr4 = sr.image_at((40, 0, 19, 30))

walk_right = [sr1, sr2, sr3, sr4]

# front walk image list
sf1 = sf.image_at((0, 0, 19, 30))
sf2 = sf.image_at((20, 0, 19, 30))
sf3 = sf.image_at((40, 0, 19, 30))
sf4 = sf.image_at((40, 0, 19, 30))

walk_front = [sf1, sf2, sf3, sf4]

# back walk image list
sb1 = sb.image_at((0, 0, 19, 30))
sb2 = sb.image_at((20, 0, 19, 30))
sb3 = sb.image_at((40, 0, 19, 30))
sb4 = sb.image_at((40, 0, 19, 30))

walk_back = [sb1, sb2, sb3, sb4]

menu = spritesheet.spritesheet("sprites/menu.png")
menu_up = menu.image_at((0, 0, 70, 100))

# get player image from spritesheet and place on map
playerImg = walk_front[0]
playerX = 96/32
playerY = 64/16
facing = "down"

# allow for player location change
playerX_change = 0
playerY_change = 0


# Draw item on screen
class Item(object):
    def __init__(self, rectangle, filename, x, y, inv):
        self.sheet = pygame.image.load(filename).convert_alpha()
        self.rectangle = rectangle
        self.X = x
        self.Y = y
        self.inv = inv

    def draw(self):
        # "Loads image from x,y,x+offset,y+offset"
        rect = pygame.Rect(self.rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pygame.RLEACCEL)
        screen.blit(image, (self.X*32, self.Y*16+8))
        return image


# define items
red_key = Item((0, 0, 32, 32), 'sprites/Keys.png', 3.5, 2, False)
yellow_key = Item((32, 0, 32, 32), 'sprites/Keys.png', 3.5, 2, False)
blue_key = Item((64, 0, 32, 32), 'sprites/Keys.png', 3.5, 2, False)
green_key = Item((96, 0, 32, 32), 'sprites/Keys.png', 3.5, 2, False)
knife = 0


# write words on the screen
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
P10 = Phrase("you have no items!", False, 10, 116, white, 10)
P11 = Phrase("Your phone is not charged!", False, 10, 116, white, 10)
P12 = Phrase("You're already dressed!", False, 10, 116, white, 10)
P13 = Phrase("Figure it out!", False, 10, 116, white, 10)

phrases = [P1, P2, P3, P4, P5, P6, P7, P8, P9, P10, P11, P12, P13]

# design the menu
menuX = 10
menuY = 10
menu_go = False
M1 = Phrase("items", False, menuX + 6, menuY + 15, black, 8)
M2 = Phrase("phone", False, menuX + 6, menuY + 35, black, 8)
M3 = Phrase("outfit", False, menuX + 6, menuY + 55, black, 8)
M4 = Phrase("guide", False, menuX + 6, menuY + 75, black, 8)
select = Phrase("-", False, menuX + 55, M1.Y, black, 8)
menu_items = [M1, M2, M3, M4, select]


# add props
class Prop(object):
    def __init__(self, rectangle, filename, x, y, move, key):
        self.sheet = pygame.image.load(filename).convert_alpha()
        self.rectangle = rectangle
        self.X = x
        self.Y = y
        self.move = move
        self.key = key

    def draw(self):
        # "Loads image from x,y,x+offset,y+offset"
        rect = pygame.Rect(self.rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pygame.RLEACCEL)
        screen.blit(image, (self.X*32, self.Y*16+8))
        return image


# define propat function for making sure player doesnt walk over box
def propat(x, y):
    for c in props:
        if x == c.X and y == c.Y:
            return True
    return False


# define props
blue_chest = Prop((0, 0, 32, 25), 'sprites/props.png', 2, 2, True, 0)
yellow_chest = Prop((32, 0, 32, 25), 'sprites/props.png', 4, 0, True, 0)
green_chest = Prop((64, 0, 32, 25), 'sprites/props.png', 5, 4, True, 0)
red_chest = Prop((96, 0, 32, 25), 'sprites/props.png', 1, 4, True, 0)
ladder = Prop((128, 25, 31, 25), 'sprites/props.png', 2, 5, False, 0)
box1 = Prop((0, 25, 31, 24), 'sprites/props.png', 6, 5, True, 3)
box2 = Prop((96, 25, 31, 24), 'sprites/props.png', 3, 5, True, 0)
box3 = Prop((32, 25, 31, 24), 'sprites/props.png', 3, 3, True, 3)
box4 = Prop((64, 25, 31, 24), 'sprites/props.png', 5, 2, True, 3)
phono = Prop((128, 0, 31, 25), 'sprites/props.png', 1, 0, False, 4)

# self.key code:
# 0: no key found for chest
# 1: key found but prop not opened
# 2: key found and prop opened
# 3: no key found for box
# 4: interact with phonograph

props = [blue_chest, yellow_chest, green_chest, red_chest, ladder, box1, box2, box3, box4, phono]


class Record(object):
    def __init__(self, audio):
        self.audio = audio

    def sing(self):
        mixer.music.load(self.audio)
        mixer.music.set_volume(0.7)
        musico = mixer.music.play(-1)
        return musico


record1 = Record("audio/record1.mp3")
record2 = Record("audio/record2.mp3")

mixer.init()
play_music = False

# set background
background_image = pygame.image.load("sprites/room.png").convert_alpha()


# create player movement function
def player(x, y):
    screen.blit(playerImg, (x+8, y))


# initialization of variables
in_room = True


red_keyX = False
blue_keyX = False
green_keyX = False
yellow_keyX = False
record = "off"


def clear():
    for c in phrases:
        c.on = False


music_start = 1

# game loop
running = True

# Draw all the props and the player
def big_draw():
    # Background Image
    screen.blit(background_image, [0, 0])

    for p in props:
        if p.Y <= playerY:
            if p.Y == 0:
                p.draw()
    for p in props:
        if p.Y <= playerY:
            if p.Y == 1:
                p.draw()
    for p in props:
        if p.Y <= playerY:
            if p.Y == 2:
                p.draw()
    for p in props:
        if p.Y <= playerY:
            if p.Y == 3:
                p.draw()
    for p in props:
        if p.Y <= playerY:
            if p.Y == 4:
                p.draw()
    for p in props:
        if p.Y <= playerY:
            if p.Y == 5:
                p.draw()
    for p in props:
        if p.Y <= playerY:
            if p.Y == 6:
                p.draw()

    player(playerX * 32, playerY * 16)

    for p in props:
        if p.Y > playerY:
            if p.Y == 0:
                p.draw()
    for p in props:
        if p.Y > playerY:
            if p.Y == 1:
                p.draw()
    for p in props:
        if p.Y > playerY:
            if p.Y == 2:
                p.draw()
    for p in props:
        if p.Y > playerY:
            if p.Y == 3:
                p.draw()
    for p in props:
        if p.Y > playerY:
            if p.Y == 4:
                p.draw()
    for p in props:
        if p.Y > playerY:
            if p.Y == 5:
                p.draw()
    for p in props:
        if p.Y > playerY:
            if p.Y == 6:
                p.draw()

    for w in phrases:
        if w.on == True:
            w.write()

    if red_keyX == True:
        red_key.draw()

while running:

    # Background Image
    screen.blit(background_image, [0, 0])

    # Event Acceptance
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether right or left
        if event.type == pygame.KEYDOWN:

            # clear any text
            clear()
            red_keyX = False

            # player movement on grid
            if event.key == pygame.K_LEFT:
                playerImg = walk_left[0]
                facing = "left"

                if not propat(playerX-1, playerY) \
                and ((playerX >= 2) or (playerX == 1 and playerY == 4)):
                    playerX += -1

            if event.key == pygame.K_RIGHT:
                playerImg = walk_right[0]
                facing = "right"

                if not propat(playerX+1, playerY) \
                and (playerX != 6 and (playerX != 0 or (playerX == 0 and playerY == 4))):
                    playerX += 1

            if event.key == pygame.K_DOWN:
                playerImg = sf.image_at((0, 0, 19, 30))
                facing = "down"
                if not propat(playerX, playerY+1) \
                and ((playerY != 5 and playerX > 0) or (playerY != 6 and playerX == 0)):
                    playerY += 1

            if event.key == pygame.K_UP:
                playerImg = sb.image_at((0, 0, 19, 30))
                facing = "up"
                if not propat(playerX, playerY-1) and playerY != 0:
                    playerY += -1

            # Track movement
            print("Keystroke pressed")
            print(facing)
            print(playerX, playerY)

            # open chests and cardboard boxes
            for target in props:
                if event.key == pygame.K_RETURN:
                    if facing == "up" and target.X == playerX and target.Y == playerY-1 and target.key == 1:
                        print("the chest opened!")
                        P1.on = True
                        target.key = 2

                    if facing == "up" and target.X == playerX and target.Y == playerY - 1 and target.key == 4 \
                    and record == "off":
                        print("You put on a record")
                        P8.on = True
                        play_music = True
                        record = "on"

                    elif facing == "up" and target.X == playerX and target.Y == playerY - 1 and target.key == 4 \
                    and record == "on":
                        print("You stopped the record")
                        music_start = 1
                        P9.on = True
                        play_music = False
                        record = "off"

                    if ((facing == "up" and target.X == playerX and target.Y == playerY - 1)
                      or (facing == "down" and target.X == playerX and target.Y == playerY + 1)
                      or (facing == "left" and target.X == playerX - 1 and target.Y == playerY)
                      or (facing == "right" and target.X == playerX + 1 and target.Y == playerY)) and target.key == 3:
                        print("the cardboard box opened!")
                        P7.on = True
                        target.key = 2

                if event.key == pygame.K_8:
                    if facing == "up" and target.X == playerX and target.Y == playerY - 1 and target.key == 4 \
                    and record == "off":
                        print("You put on a record")
                        P8.on = True
                        music_start = 3
                        play_music = True
                        record = "on"

                    elif facing == "up" and target.X == playerX and target.Y == playerY - 1 and target.key == 4 \
                    and record == "on":
                        print("You stopped the record")
                        P9.on = True
                        play_music = False
                        record = "off"

                    # if facing == "up" and target.X == playerX and target.Y == playerY - 1 and target.key == 5:
                    #     print("You put on a record")
                    #     clear()
                    #     P9.on = True
                    #     target.key = 4

            # push props forward
            if event.key == pygame.K_SPACE:
                for target in props:
                    if facing == "left" and playerX-1 == target.X and playerY == target.Y \
                    and not propat(playerX-2, playerY) and target.X > 1 and target.move == True:
                        target.X -= 1

                    if facing == "right" and playerX+1 == target.X and playerY == target.Y \
                    and not propat(playerX+2, playerY) and target.X < 6 and target.move == True:
                        target.X += 1

                    if facing == "down" and playerX == target.X and playerY+1 == target.Y \
                    and not propat(playerX, playerY+2) and target.Y < 5:
                        target.Y += 1

                    if facing == "up" and playerX == target.X and playerY-1 == target.Y \
                    and not propat(playerX, playerY-2) and target.Y > 0 and target.move == True:
                        target.Y -= 1

            # Pull props around
            if event.key == pygame.K_BACKSPACE:
                for target in props:
                    if facing == "left" and playerX-1 == target.X and playerY == target.Y \
                    and not propat(playerX+1, playerY) and playerX < 6 and target.move == True:
                        playerX += 1
                        target.X += 1

                    if facing == "right" and playerX+1 == target.X and playerY == target.Y \
                    and not propat(playerX-1, playerY) and playerX > 1 and target.move == True:
                        playerX -= 1
                        target.X -= 1

                    if facing == "up" and playerX == target.X and playerY-1 == target.Y \
                    and not propat(playerX, playerY+1) and playerY < 5 and target.move == True:
                        playerY += 1
                        target.Y += 1

                    if facing == "down" and playerX == target.X and playerY+1 == target.Y \
                    and not propat(playerX, playerY-1) and playerY > 0 and target.move == True:
                        playerY -= 1
                        target.Y -= 1

            if event.key == pygame.K_LCTRL and menu_go == False:
                menu_go = True

            # Find Keys
            if event.key == pygame.K_0:
                red_keyX = True
                red_chest.key = 1
                print("You found a red key!")
                P3.on = True

            if event.key == pygame.K_1:
                blue_keyX = True
                blue_chest.key = 1
                print("You found a blue key")
                P4.on = True

            if event.key == pygame.K_2:
                green_keyX = True
                green_chest.key = 1
                print("You found a green key!")
                P5.on = True

            if event.key == pygame.K_3:
                yellow_keyX = True
                yellow_chest.key = 1
                print("You found a yellow key!")
                P6.on = True

        # Release Keys
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # switch between in room and crawlspace
    if playerX == 0 and playerY == 4:
        in_room = False
    if playerX == 1 and playerY == 4:
        in_room = True

    playerX += playerX_change
    playerY += playerY_change

    big_draw()

    if music_start == 1:
        record1.sing()
        music_start = 2

    if music_start == 3:
        record2.sing()
        music_start = 2

    if play_music == True:
        mixer.music.unpause()

    if play_music == False:
        mixer.music.pause()

    while menu_go == True:
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                clear()
                print(P10.on)

                if event.key == pygame.K_EQUALS:
                    menu_go = False

                if event.key == pygame.K_DOWN and select.Y == M1.Y:
                    select.Y = M2.Y
                elif event.key == pygame.K_DOWN and select.Y == M2.Y:
                    select.Y = M3.Y
                elif event.key == pygame.K_DOWN and select.Y == M3.Y:
                    select.Y = M4.Y
                elif event.key == pygame.K_DOWN and select.Y == M4.Y:
                    select.Y = M1.Y

                if event.key == pygame.K_UP and select.Y == M1.Y:
                    select.Y = M4.Y
                elif event.key == pygame.K_UP and select.Y == M2.Y:
                    select.Y = M1.Y
                elif event.key == pygame.K_UP and select.Y == M3.Y:
                    select.Y = M2.Y
                elif event.key == pygame.K_UP and select.Y == M4.Y:
                    select.Y = M3.Y

                if event.key == pygame.K_RETURN and select.Y == M1.Y:
                    print("you have no items!")
                    P10.on = True
                    print(P10.on)

                elif event.key == pygame.K_RETURN and select.Y == M2.Y:
                    print("Phone is out of batteries!")
                    P11.on = True
                    print(P10.on)

                elif event.key == pygame.K_RETURN and select.Y == M3.Y:
                    print("You're already wearing clothes!")
                    P12.on = True
                    print(P10.on)

                elif event.key == pygame.K_RETURN and select.Y == M4.Y:
                    print("Figure it out?!")
                    P13.on = True
                    print(P10.on)

        big_draw()
        screen.blit(menu_up, (menuX, menuY))
        for m in menu_items:
            m.write()

        pygame.display.update()
        clock.tick(5)

    pygame.display.update()

    clock.tick(5)