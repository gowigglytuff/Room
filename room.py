import pygame
import spritesheet
from pygame import mixer
from sprites import *

# initialize pygame
pygame.init()

pygame.display.set_caption('Room')
clock = pygame.time.Clock()

# create screen
screen = pygame.display.set_mode((256, 128))

tileX = 32
tileY = 16

black = (0, 0, 0)
white = (255, 255, 255)
green = (3, 87, 43)

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

# Mouse Img
mouse_left = spritesheet.spritesheet('sprites/mouse.png').image_at((0, 0, 19, 30))
mouse_back = spritesheet.spritesheet('sprites/mouse.png').image_at((20, 0, 19, 30))
mouse_right = spritesheet.spritesheet('sprites/mouse.png').image_at((40, 0, 19, 30))
mouse_front = spritesheet.spritesheet('sprites/mouse.png').image_at((40, 0, 19, 30))

# design the menu
menuX = 10
menuY = 10

# Menu spacing
MIX = menuX + 6
menu_size = (100-20)
menu_number = 5
spacing = menu_size/menu_number
menu_start = menuY + 15
menu_end = menuY +75

MIY1 = menu_start
MIY2 = menu_start + spacing
MIY3 = menu_start + (spacing*2)
MIY4 = menu_start + (spacing*3)
MIY5 = menu_start + (spacing*4)

menu = spritesheet.spritesheet("sprites/menu.png")
menu_up = menu.image_at((0, 0, 70, 100))

# get player image from spritesheet and place on map
playerImg = walk_front[0]
playerX = 96/tileX
playerY = 64/tileY
facing = "down"


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


# phrases for bottom left of screen
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
P14 = Phrase("You looked inside!", False, 10, 116, white, 10)
P15 = Phrase("You can't use that now!", False, 10, 116, white, 10)
P16 = Phrase("The chest is locked!!", False, 10, 116, white, 10)
P17 = Phrase("Better not leave yet...", False, 10, 116, white, 10)
P18 = Phrase("Can't get the tape off...", False, 10, 116, white, 10)

# Taps
P19 = Phrase("It's brightly coloured...", False, 10, 116, white, 10)
P20 = Phrase("It's very sharp!", False, 10, 116, white, 10)

P21 = Phrase("Aw, it's cute!", False, 10, 116, white, 10)

phrases = [P1, P2, P3, P4, P5, P6, P7, P8, P9, P10, P11, P12, P13, P14, P15, P16, P17, P18, P19, P20, P21]



M1 = Phrase("items", False, MIX, MIY1, black, 8)
M2 = Phrase("phone", False, MIX, MIY2, black, 8)
M3 = Phrase("outfit", False, MIX, MIY3, black, 8)
M4 = Phrase("scraps", False, MIX, MIY4, black, 8)
M5 = Phrase("esc", False, MIX, MIY5, black, 8)

menu_items = [M1, M2, M3, M4, M5]

# phrases for selector
select = Phrase("-", False, menuX + 55, MIY1, black, 8)

# phrases for inventory
I0 = Phrase("esc", False, MIX, MIY5, black, 8)
I1 = Phrase("r. key", False, MIX, MIY1, black, 8)
I2 = Phrase("y. key", False, MIX, MIY2, black, 8)
I3 = Phrase("b. key", False, MIX, MIY3, black, 8)
I4 = Phrase("g. key", False, MIX, MIY4, black, 8)
I5 = Phrase("knife", False, MIX, MIY1, black, 8)
I6 = Phrase("dolly", False, MIX, MIY3, black, 8)
I7a = Phrase("partx1", False, MIX, MIY1, black, 8)
I7b = Phrase("partx2", False, MIX, MIY1, black, 8)
I7c = Phrase("partx3", False, MIX, MIY1, black, 8)
I8 = Phrase("duster", False, MIX, MIY2, black, 8)
I9 = Phrase("snack", False, MIX, MIY3, black, 8)
I10 = Phrase("kettle", False, MIX, MIY4, black, 8)
I11 = Phrase("toy", False, MIX, MIY4, black, 8)
I12 = Phrase("bobble", False, MIX, MIY2, black, 8)

inventory = [I1, I2, I3, I4, I5, I6, I7a, I7b, I7c, I8, I9]

# phrases for scraps
S1 = Phrase("The rats are dancing to jazz", False, menuX + 6, menuY + 15, black, 8)
S2 = Phrase("My knees are getting old", False, menuX + 6, menuY + 15, black, 8)
S3 = Phrase("Bees are friendly", False, menuX + 6, menuY + 15, black, 8)
S4 = Phrase("I'm not sure where Hue is", False, menuX + 6, menuY + 15, black, 8)

rambling = [S1, S2, S3, S4]
total_scraps = (4-1)

T1a = Phrase("Hi sweetie, hope things", False, menuX + 16, menuY + 35, green, 8)
T2a = Phrase("Did you find anything cool?", False, menuX + 16, menuY + 35, green, 8)
T3a = Phrase("message me if you need", False, menuX + 16, menuY + 35, green, 8)

T1b = Phrase("are going okay.", False, menuX + 16, menuY + 55, green, 8)
T2b = Phrase(" ", False, menuX + 16, menuY + 55, green, 8)
T3b = Phrase("any help with anything!", False, menuX + 16, menuY + 55, green, 8)

texts = [T1a, T2a, T3a]
textsb = [T1b, T2b, T3b]
total_texts = (3-1)

SM1 = Phrase("use", False, menuX + 76, menuY + 10, black, 8)
SM2 = Phrase("tap", False, menuX + 76, menuY + 22, black, 7)
SM3 = Phrase("esc", False, menuX + 76, menuY + 34, black, 8)

subpicks = [SM1, SM2, SM3]

subselect = Phrase("-", False, SM1.X + 25, SM1.Y, black, 8)

# define items
# Draw item on screen
class Item(object):
    def __init__(self, rectangle, filename, x, y, inv, phrase, page):
        self.sheet = pygame.image.load(filename).convert_alpha()
        self.rectangle = rectangle
        self.X = x
        self.Y = y
        self.inv = inv
        self.phrase = phrase
        self.page = page


    def draw(self):
        # "Loads image from x,y,x+offset,y+offset"
        rect = pygame.Rect(self.rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pygame.RLEACCEL)
        screen.blit(image, (self.X*tileX, self.Y*tileY+(tileY/2)))
        return image


# list of items to appear in inventory
red_key = Item((0, 0, 32, 32), 'sprites/Keys.png', 3.5, 2, True, I1, 1)
yellow_key = Item((32, 0, 32, 32), 'sprites/Keys.png', 3.5, 2, True, I2, 1)
blue_key = Item((64, 0, 32, 32), 'sprites/Keys.png', 3.5, 2, True, I3, 1)
green_key = Item((96, 0, 32, 32), 'sprites/Keys.png', 3.5, 2, True, I4, 1)
knife = Item((96, 0, 32, 32), 'sprites/Keys.png', 3.5, 2, True, I5, 2)
dolly = Item((96, 0, 32, 32), 'sprites/Keys.png', 3.5, 2, True, I6, 2)
machine1 = Item((96, 0, 32, 32), 'sprites/Keys.png', 3.5, 2, True, I7a, 3)
duster = Item((96, 0, 32, 32), 'sprites/Keys.png', 3.5, 2, True, I8, 3)
snack = Item((96, 0, 32, 32), 'sprites/Keys.png', 3.5, 2, True, I9, 3)
kettle = Item((96, 0, 32, 32), 'sprites/Keys.png', 3.5, 2, True, I10, 3)
toy = Item((96, 0, 32, 32), 'sprites/Keys.png', 3.5, 2, True, I11, 2)
bobble = Item((96, 0, 32, 32), 'sprites/Keys.png', 3.5, 2, True, I12, 2)

items = [red_key, yellow_key, blue_key, green_key, knife, dolly, machine1, duster, snack, kettle, toy, bobble]

current_inv = [red_key, yellow_key, blue_key, green_key, knife, dolly,
               machine1, duster, snack, kettle, toy, bobble]


# define props
class Prop(object):
    def __init__(self, rectangle, filename, x, y, move, key, on):
        self.sheet = pygame.image.load(filename).convert_alpha()
        self.rectangle = rectangle
        self.X = x
        self.Y = y
        self.move = move
        self.key = key
        self.on = on

    def draw(self):
        # "Loads image from x,y,x+offset,y+offset"
        rect = pygame.Rect(self.rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pygame.RLEACCEL)
        screen.blit(image, (self.X*tileX, self.Y*tileY+(tileY/2)))
        return image

    def drawmouse(self):
        # "Loads image from x,y,x+offset,y+offset"
        rect = pygame.Rect(self.rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pygame.RLEACCEL)
        screen.blit(image, ((self.X*tileX)+8, self.Y*tileY))
        return image

# define propat function for making sure player doesnt walk over box
def propat(x, y):
    for c in propslist:
        if x == c.X and y == c.Y and c.on == True:
            return True
    return False


# list of props that appear in the room
blue_chest = Prop((0, 0, 32, 25), 'sprites/props.png', 2, 2, True, 0, True)
yellow_chest = Prop((32, 0, 32, 25), 'sprites/props.png', 4, 0, True, 0, True)
green_chest = Prop((64, 0, 32, 25), 'sprites/props.png', 5, 4, True, 0, True)
red_chest = Prop((96, 0, 32, 25), 'sprites/props.png', 3, 3, True, 0, True)
ladder = Prop((128, 25, 31, 25), 'sprites/props.png', 2, 5, False, 6, True)
box1 = Prop((0, 25, 31, 24), 'sprites/props.png', 6, 5, True, 5, True)
box2 = Prop((96, 25, 31, 24), 'sprites/props.png', 3, 5, True, 5, True)
box3 = Prop((32, 25, 31, 24), 'sprites/props.png', 1, 4, True, 3, True)
box4 = Prop((64, 25, 31, 24), 'sprites/props.png', 5, 2, True, 3, True)
phono = Prop((128, 0, 31, 25), 'sprites/props.png', 1, 0, False, 4, True)

# list of images to be displayed that are not props
scrap = Prop((0, 0, 256, 128), "sprites/scrap.png", 0, -0.5, False, 0, False)

phone_bg = Prop((0, 0, 256, 128), "sprites/phone.png", 0, -0.5, False, 0, False)

submenu = Prop((0, 0, 45, 50), "sprites/submenu.png", 80/32, 2/16, False, 0, False)

mousey = Prop((0, 0, 19, 30), "sprites/mouse.png", 4, 0, False, 100, False)

# self.key code:
# 0: no key found for chest
# 1: key found but prop not opened
# 2: key found and prop opened
# 3: no key found for box
# 4: interact with phonograph
# 5: Box opened
# 6: ladder


props = [blue_chest, yellow_chest, green_chest, red_chest, ladder, box1, box2, box3, box4, phono]
propslist = [blue_chest, yellow_chest, green_chest, red_chest, ladder, box1, box2, box3, box4, phono, mousey]

# define record
class Record(object):
    def __init__(self, audio):
        self.audio = audio

    def sing(self):
        mixer.music.load(self.audio)
        mixer.music.set_volume(0.7)
        musico = mixer.music.play(-1)
        return musico


# list of available records
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
FPS = 5
in_room = True
red_keyX = False
blue_keyX = False
green_keyX = False
yellow_keyX = False
record = "off"
menu_go = False
in_menu = False
in_inv = False
in_scrap = False
in_phone = False
list_select = 0
select4 = 0
in_submenu = False
inv_page = 1
pause = True
mouse_tick = 0
mouse_ticking = True
mouse_stay = False

def clear():
    for c in phrases:
        c.on = False


def clear_scrap():
    for s in rambling:
        s.on = False

def clear_texts():
    for t in texts:
        t.on = False
    for t in textsb:
        t.on = False

def clear_menu():
    global in_menu, in_inv, in_scrap, menu_go, in_phone, in_submenu, inv_page
    scrap.on = False
    in_menu = False
    in_inv = False
    in_scrap = False
    menu_go = False
    phone_bg.on = False
    in_phone = False
    for m in menu_items:
        m.on = False
    select.on = False
    select.Y = MIY1
    subselect.on = False
    subselect.Y = SM1.Y
    in_submenu = False
    for o in current_inv:
        o.phrase.on = False
    inv_page = 1


music_start = 1

# game loop
running = True


# Draw all the props and the player
def big_draw():
    # Background Image
    screen.blit(background_image, [0, 0])

    if mousey.on == True:
        mousey.drawmouse()

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

    player(playerX * tileX, playerY * tileY)

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

    if scrap.on == True:
        scrap.draw()

    if phone_bg.on == True:
        phone_bg.draw()


def menu_draw():
    if in_menu == True or in_inv == True or in_submenu == True:
        screen.blit(menu_up, (menuX, menuY))
        if select.on == True:
            select.write()

    if in_submenu == True:
        submenu.draw()
        for s in subpicks:
            s.write()
        if subselect.on == True:
            subselect.write()
        for m in current_inv:
            if m.phrase.on == True:
                m.phrase.write()
        if I0.on == True:
            I0.write()

    for m in menu_items:
        if m.on == True:
            m.write()

    if in_inv == True:
        for m in current_inv:
            if m.phrase.on == True:
                m.phrase.write()
        if I0.on == True:
            I0.write()

    if in_scrap == True:
        for r in rambling:
            if r.on == True:
                r.write()
    if in_phone == True:
        for r in texts:
            if r.on == True:
                r.write()
        for r in textsb:
            if r.on == True:
                r.write()


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

# interact with mousey
            if event.key == pygame.K_RETURN:
                if ((facing == "up" and mousey.X == playerX and mousey.Y == playerY - 1)
                    or (facing == "down" and mousey.X == playerX and mousey.Y == playerY + 1)
                    or (facing == "left" and mousey.X == playerX - 1 and mousey.Y == playerY)
                    or (facing == "right" and mousey.X == playerX + 1 and mousey.Y == playerY))\
                        and mousey.on == True:
                        P21.on = True

            # open chests and cardboard boxes
            for target in props:
                if event.key == pygame.K_RETURN:
                    if facing == "up" and target.X == playerX and target.Y == playerY - 1:
                        if target.key == 2:
                            print("you looked inside")
                            P14.on = True
                        if target.key == 0:
                            print("the chest is locked")
                            P16.on = True

                    if ((facing == "up" and target.X == playerX and target.Y == playerY - 1)
                        or (facing == "down" and target.X == playerX and target.Y == playerY + 1)
                        or (facing == "left" and target.X == playerX - 1 and target.Y == playerY)
                        or (facing == "right" and target.X == playerX + 1 and target.Y == playerY)) \
                        and target.key == 5:
                            print("you looked inside")
                            P14.on = True
                    if ((facing == "up" and target.X == playerX and target.Y == playerY - 1)
                        or (facing == "down" and target.X == playerX and target.Y == playerY + 1)
                        or (facing == "left" and target.X == playerX - 1 and target.Y == playerY)
                        or (facing == "right" and target.X == playerX + 1 and target.Y == playerY)) \
                        and target.key == 6:
                            print("better not leave until we're finished!")
                            P17.on = True
                    if ((facing == "up" and target.X == playerX and target.Y == playerY - 1)
                        or (facing == "down" and target.X == playerX and target.Y == playerY + 1)
                        or (facing == "left" and target.X == playerX - 1 and target.Y == playerY)
                        or (facing == "right" and target.X == playerX + 1 and target.Y == playerY)) \
                        and target.key == 3:
                            print("Can't get the tape off...")
                            P18.on = True

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
                        mouse_stay = False

                # Play record 2
                if event.key == pygame.K_8:
                    if facing == "up" and target.X == playerX and target.Y == playerY - 1 and target.key == 4:
                        if record == "off":
                            print("You put on a record")
                            P8.on = True
                            music_start = 3
                            play_music = True
                            record = "on"
                            mouse_stay = True

                        elif record == "on":
                            print("You stopped the record")
                            P9.on = True
                            play_music = False
                            record = "off"
                            mouse_stay = False

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

            # Open Menu
            if event.key == pygame.K_LCTRL and menu_go == False:
                menu_go = True
                for m in menu_items:
                    m.on = True
                in_menu = True
                select.on = True

            # Find Keys
            if event.key == pygame.K_0:
                red_keyX = True
                red_chest.key = 1
                print("You found a red key!")
                P3.on = True
                red_key.inv = True
                current_inv.append(red_key)

            if event.key == pygame.K_1:
                blue_keyX = True
                blue_chest.key = 1
                print("You found a blue key")
                P4.on = True
                blue_key.inv = True
                current_inv.append(blue_key)

            if event.key == pygame.K_2:
                green_keyX = True
                green_chest.key = 1
                print("You found a green key!")
                P5.on = True
                green_key.inv = True
                current_inv.append(green_key)

            if event.key == pygame.K_3:
                yellow_keyX = True
                yellow_chest.key = 1
                print("You found a yellow key!")
                P6.on = True
                yellow_key.inv = True
                current_inv.append(yellow_key)

        # Release Keys
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    for f in props:
        if f.X != 4 and f.Y != 0:
            if playerY > 2 or playerX < 3 or playerX > 5:
                mousey.on = True
                print("hmm")

    if (playerX == 3 or playerX == 4 or playerX == 5)and playerY < 3 and mouse_stay == False:
        mousey.on = False


# mouse animations
    if mouse_ticking == True:
        mouse_tick += 1
        if mouse_tick == 5:
            mousey.rectangle = (0, 0, 19, 30)
        if mouse_tick == 10:
            mousey.rectangle = (19, 0, 19, 30)
        if mouse_tick == 15:
            mousey.rectangle = (38, 0, 19, 30)
        if mouse_tick == 20:
            mousey.rectangle = (57, 0, 19, 30)
            mouse_tick = 1

    # switch between in room and crawlspace
    if playerX == 0 and playerY == 4:
        in_room = False
    if playerX == 1 and playerY == 4:
        in_room = True

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
            if event.type == pygame.QUIT:
                running = False
                menu_go = False

            if event.type == pygame.KEYDOWN:
                clear()
                print(P10.on)

                if event.key == pygame.K_LCTRL:
                    clear_menu()

                if in_menu == True:
                    menu_number = 5

                    if event.key == pygame.K_DOWN and select.Y == M1.Y:
                        select.Y = M2.Y
                    elif event.key == pygame.K_DOWN and select.Y == M2.Y:
                        select.Y = M3.Y
                    elif event.key == pygame.K_DOWN and select.Y == M3.Y:
                        select.Y = M4.Y
                    elif event.key == pygame.K_DOWN and select.Y == M4.Y:
                        select.Y = M5.Y
                    elif event.key == pygame.K_DOWN and select.Y == M5.Y:
                        select.Y = M1.Y

                    if event.key == pygame.K_UP and select.Y == M1.Y:
                        select.Y = M5.Y
                    elif event.key == pygame.K_UP and select.Y == M2.Y:
                        select.Y = M1.Y
                    elif event.key == pygame.K_UP and select.Y == M3.Y:
                        select.Y = M2.Y
                    elif event.key == pygame.K_UP and select.Y == M4.Y:
                        select.Y = M3.Y
                    elif event.key == pygame.K_UP and select.Y == M5.Y:
                        select.Y = M4.Y

                    # inventory
                    if event.key == pygame.K_RETURN and select.Y == M1.Y:
                        print("you have no items!")
                        P10.on = True
                        for m in current_inv:
                            if m.page == 1:
                                m.phrase.on = True
                        for m in menu_items:
                            m.on = False
                        in_menu = False
                        in_inv = True
                        I0.on = True
                        pause = False

                    # phone
                    elif event.key == pygame.K_RETURN and select.Y == M2.Y:
                        in_phone = True
                        phone_bg.on = True
                        for m in menu_items:
                            m.on = False
                        in_menu = False
                        T1a.on = True
                        T1b.on = True

                    # outfit
                    elif event.key == pygame.K_RETURN and select.Y == M3.Y:
                        print("You're already wearing clothes!")
                        P12.on = True

                    # scraps
                    elif event.key == pygame.K_RETURN and select.Y == M4.Y:
                        scrap.on = True
                        for m in menu_items:
                            m.on = False
                        in_menu = False
                        in_scrap = True
                        S1.on = True

                    # escape
                    elif event.key == pygame.K_RETURN and select.Y == M5.Y:
                        clear_menu()
# in scraps
                if in_scrap == True:
                    if event.key == pygame.K_DOWN:
                        in_scrap = False
                        scrap.on = False
                        in_menu = True
                        list_select = 0
                        for m in menu_items:
                            m.on = True
                        clear_scrap()

                    if event.key == pygame.K_RIGHT and list_select < total_scraps:
                        clear_scrap()
                        list_select += 1
                        (rambling[list_select]).on = True

                    if event.key == pygame.K_LEFT and list_select > 0:
                        clear_scrap()
                        list_select -= 1
                        (rambling[list_select]).on = True
# in phone
                if in_phone == True:
                    if event.key == pygame.K_DOWN:
                        in_phone = False
                        phone_bg.on = False
                        in_menu = True
                        list_select = 0
                        for m in menu_items:
                            m.on = True
                        clear_texts()

                    if event.key == pygame.K_RIGHT and list_select < total_texts:
                        clear_texts()
                        list_select += 1
                        (texts[list_select]).on = True
                        (textsb[list_select]).on = True

                    if event.key == pygame.K_LEFT and list_select > 0:
                        clear_texts()
                        list_select -= 1
                        (texts[list_select]).on = True
                        (textsb[list_select]).on = True
# in inventory
                if in_inv == True:
                    menu_number = 4

                    if event.key == pygame.K_DOWN:
                        if select.Y == MIY1:
                            select.Y = M2.Y
                        elif select.Y == MIY2:
                            select.Y = M3.Y
                        elif select.Y == MIY3:
                            select.Y = M4.Y
                        elif select.Y == MIY4:
                            select.Y = M5.Y
                        elif select.Y == MIY5:
                            select.Y = M1.Y

                    if event.key == pygame.K_UP:
                        if select.Y == M1.Y:
                            select.Y = M5.Y
                        elif select.Y == M2.Y:
                            select.Y = M1.Y
                        elif select.Y == M3.Y:
                            select.Y = M2.Y
                        elif select.Y == M4.Y:
                            select.Y = M3.Y
                        elif select.Y == M5.Y:
                            select.Y = M4.Y

                    if event.key == pygame.K_RIGHT:
                        if inv_page == 1:
                            inv_page = 2
                            for m in current_inv:
                                if m.page == 1 or 3:
                                    m.phrase.on = False
                            for m in current_inv:
                                if m.page == 2:
                                    m.phrase.on = True
                        elif inv_page == 2:
                            inv_page = 3
                            for m in current_inv:
                                if m.page == 2 or 1:
                                    m.phrase.on = False
                            for m in current_inv:
                                if m.page == 3:
                                    m.phrase.on = True
                        elif inv_page == 3:
                            inv_page = 1
                            for m in current_inv:
                                if m.page == 3 or 2:
                                    m.phrase.on = False
                            for m in current_inv:
                                if m.page == 1:
                                    m.phrase.on = True

                    if event.key == pygame.K_LEFT:
                        if inv_page == 1:
                            inv_page = 3
                            for m in current_inv:
                                if m.page == 1:
                                    m.phrase.on = False
                            for m in current_inv:
                                if m.page == 3:
                                    m.phrase.on = True
                        elif inv_page == 2:
                            inv_page = 1
                            for m in current_inv:
                                if m.page == 2:
                                    m.phrase.on = False
                            for m in current_inv:
                                if m.page == 1:
                                    m.phrase.on = True
                        elif inv_page == 3:
                            inv_page = 2
                            for m in current_inv:
                                if m.page == 3:
                                    m.phrase.on = False
                            for m in current_inv:
                                if m.page == 2:
                                    m.phrase.on = True

                    if event.key == pygame.K_RETURN and pause == True:
                        if select.Y == MIY5:
                            in_inv = False
                            in_menu = True
                            for m in menu_items:
                                m.on = True
                            clear_texts()
                            for m in current_inv:
                                m.phrase.on = False
                            I0.on = False
                        else:
                            for i in current_inv:
                                if i.page == inv_page and i.inv == True and i.phrase.Y == select.Y:
                                    if select.Y == MIY1:
                                        select.on = False
                                        in_submenu = True
                                        in_inv = False
                                        pause = False
                                        subselect.on = True
                                    if select.Y == MIY2:
                                        select.on = False
                                        in_submenu = True
                                        in_inv = False
                                        pause = False
                                        subselect.on = True
                                    if select.Y == MIY3:
                                        select.on = False
                                        in_submenu = True
                                        in_inv = False
                                        pause = False
                                        subselect.on = True
                                    if select.Y == MIY4:
                                        select.on = False
                                        in_submenu = True
                                        in_inv = False
                                        pause = False
                                        subselect.on = True
# in submenu
                if in_submenu == True:
                    if event.key == pygame.K_DOWN:
                        if subselect.Y == SM1.Y:
                            subselect.Y = SM2.Y
                        elif subselect.Y == SM2.Y:
                            subselect.Y = SM3.Y
                        elif subselect.Y == SM3.Y:
                            subselect.Y = SM1.Y
                    if event.key == pygame.K_UP:
                        if subselect.Y == SM1.Y:
                            subselect.Y = SM3.Y
                        elif subselect.Y == SM2.Y:
                            subselect.Y = SM1.Y
                        elif subselect.Y == SM3.Y:
                            subselect.Y = SM2.Y
                    if event.key == pygame.K_RETURN and pause == True:
                        if subselect.Y == SM3.Y:
                            in_inv = True
                            in_submenu = False
                            select.on = True
                            subselect.on = False
# submenu "tap" button
                        if subselect.Y == SM2.Y:
                            if inv_page == 1:
                                if select.Y == MIY1 or MIY2 or MIY3 or MIY4:
                                    P19.on = True
                                    print("I wonder if the colour means anything...")
                            if inv_page == 2:
                                if select.Y == MIY1:
                                    print("It's very sharp!")
                                    P20.on = True

# submenu "use" button
                        if subselect.Y == SM1.Y:
                            if inv_page == 1:
                                if select.Y == MIY1:
                                    if facing == "up" and red_chest.X == playerX and red_chest.Y == playerY - 1:
                                        print("the chest opened!")
                                        P1.on = True
                                        red_chest.key = 2
                                        clear_menu()
                                    else:
                                        print("you can't use that now...")
                                        P15.on = True
                                        in_inv = True
                                        in_submenu = False
                                        select.on = True
                                        subselect.on = False
                                elif select.Y == MIY2:
                                    if facing == "up" and yellow_chest.X == playerX and yellow_chest.Y == playerY - 1:
                                        P1.on = True
                                        yellow_chest.key = 2
                                        print("the chest opened!")
                                        clear_menu()
                                    else:
                                        print("you can't use that now...")
                                        P15.on = True
                                        in_inv = True
                                        in_submenu = False
                                        select.on = True
                                        subselect.on = False
                                elif select.Y == MIY3:
                                    if facing == "up" and blue_chest.X == playerX and blue_chest.Y == playerY - 1:
                                        P1.on = True
                                        blue_chest.key = 2
                                        print("the chest opened!")
                                        clear_menu()
                                    else:
                                        print("you can't use that now...")
                                        P15.on = True
                                        in_inv = True
                                        in_submenu = False
                                        select.on = True
                                        subselect.on = False
                                elif select.Y == MIY4:
                                    if facing == "up" and green_chest.X == playerX and green_chest.Y == playerY - 1:
                                        P1.on = True
                                        green_chest.key = 2
                                        print("the chest opened!")
                                        clear_menu()
                                    else:
                                        print("you can't use that now...")
                                        P15.on = True
                                        in_inv = True
                                        in_submenu = False
                                        select.on = True
                                        subselect.on = False
                            if inv_page == 2:
                                if select.Y == MIY1:
                                    for target in props:
                                        if ((facing == "up" and target.X == playerX and target.Y == playerY - 1)
                                            or (facing == "down" and target.X == playerX and target.Y == playerY + 1)
                                            or (facing == "left" and target.X == playerX - 1 and target.Y == playerY)
                                            or (facing == "right" and target.X == playerX + 1 and target.Y == playerY)):
                                                if target.key == 3:
                                                    print("the cardboard box opened!")
                                                    P7.on = True
                                                    target.key = 5
                                                    clear_menu()
                                                    for m in current_inv:
                                                        m.phrase.on = False
                                                elif target.key != 3:
                                                    print("you can't use that now...")
                                                    P15.on = True
                                                    in_inv = True
                                                    in_submenu = False
                                                    select.on = True
                                                    subselect.on = False
        print(inv_page)
        pause = True
        big_draw()
        menu_draw()
        pygame.display.update()
        clock.tick(5)

    pygame.display.update()

    clock.tick(FPS)
