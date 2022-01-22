import pygame
import random
import sys
import math

from material import image as img
from material import audio as aud
# Pygame Setup
pygame.init()


clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 1000)

pixel_per_block = img.pixel_per_block
velocity_fix = pixel_per_block / 64
sight_block_row = 9
sight_block_column = 15

screen_width = sight_block_column * pixel_per_block  # 15 * 64 = 960
screen_height = sight_block_row * pixel_per_block  # 9 * 64 = 576

screen = pygame.display.set_mode((screen_width, screen_height))
toolBar_surface = pygame.Surface((344, 64))
buffer_surface = pygame.Surface(
    (pixel_per_block * sight_block_column, pixel_per_block * sight_block_row))
pygame.display.set_caption("Dungeon")
pygame.display.set_icon(pygame.image.load("images/slime.png"))
pygame.mouse.set_visible(False)

fontSize = 20
font = pygame.font.Font('freesansbold.ttf', fontSize)
smallFont = pygame.font.Font('freesansbold.ttf', 10)
toolBarFont = pygame.font.Font('freesansbold.ttf', 15)
portalFont = pygame.font.Font('Antonio-Bold.ttf', 20)
clearLevelFont = pygame.font.Font('Antonio-Bold.ttf', 140)
tutorialFont = pygame.font.Font('Antonio-Bold.ttf', 16)

textX = sight_block_column * pixel_per_block - 95
textY = sight_block_row * pixel_per_block - 100

HOW_TO_PLAY_bg = (66, 66, 66)

# funcs


def getBase(deltaX, deltaY):
    return (deltaX ** 2 + deltaY ** 2) ** .5


def changeMap(Map):
    global currMap, mapChanged
    currMap = Map
    mapChanged = True


# Main Menu
mainMenu = True
MENU_FRAME_RATE = .1
currSprite = 0
howToPlay_counter = 0
bg = img.howToPlay_sprites[0]


while mainMenu:
    currSprite += MENU_FRAME_RATE

    bg_sprites = img.gameTitle_sprites
    if currSprite >= len(bg_sprites):
        currSprite = 0

    screen.blit(img.menuBackground, (-480, -312))
    screen.blit(bg_sprites[int(currSprite)], (80, 100))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                mainMenu = False
                aud.clickButtonSound.play()
            if event.key == pygame.K_h:
                howToPlay = True

                while howToPlay:
                    howToPlay_counter += 1
                    howToPlaybg = img.howToPlay_sprites
                    screen.fill(HOW_TO_PLAY_bg)

                    if howToPlay_counter > 9:
                        howToPlay_counter = 0
                        bg = random.choice(howToPlaybg)

                    screen.blit(bg,  (80, 100))
                    pygame.display.update()
                    for inner_event in pygame.event.get():
                        if inner_event.type == pygame.KEYDOWN:
                            howToPlay = False
                        if inner_event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


# Groups
aim = pygame.sprite.Group()

block_group = pygame.sprite.Group()

slime_group = pygame.sprite.Group()
fireball_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
effect_group = pygame.sprite.Group()
status_group = pygame.sprite.Group()
bar_group = pygame.sprite.Group()
boss_group = pygame.sprite.Group()
wand_group = pygame.sprite.Group()
staticEffect_group = pygame.sprite.Group()
electricball_group = pygame.sprite.Group()
tool_bar_group = pygame.sprite.Group()
item_drop_group = pygame.sprite.Group()
portal_group = pygame.sprite.Group()
shop_group = pygame.sprite.Group()
static_instance_group = pygame.sprite.Group()
text_display_group = pygame.sprite.Group()
npc_group = pygame.sprite.Group()
boss_health_bar_group = pygame.sprite.Group()
skeleton_pet_group = pygame.sprite.Group()
inventory_group = pygame.sprite.Group()
inventory_text = pygame.sprite.Group()


def setupSafeHouse():
    changeMap(safeHouseMap)
    portal_group.add(
        Portal(14, 2.25, 3, 4, Portal.TYPE_PURPLE_PORTAL, Portal.USAGE_SHOP))
    portal_group.add(
        Portal(14, 4.5, 1, 4, Portal.TYPE_GREEN_PORTAL, Portal.USAGE_SWEEP))
    portal_group.add(
        Portal(14, 6.75, 1, 4, Portal.TYPE_PURPLE_PORTAL, Portal.USAGE_NEXT_LEVEL))


def setupShop():
    changeMap(shopMap)
    static_instance_group.add(StaticInstance(
        5.5, 1.5, StaticInstance.TYPE_SHOP_MANA_POTION_CHEST))
    static_instance_group.add(StaticInstance(
        8.5, 1.5, StaticInstance.TYPE_SHOP_HEALTH_POTION_CHEST))
    static_instance_group.add(StaticInstance(
        11.5, 1.5, StaticInstance.TYPE_SHOP_MYSTERY_CHEST))
    portal_group.add(
        Portal(1, 4.5, 1, 4, Portal.TYPE_GREEN_PORTAL, Portal.USAGE_BACK_FROM_SHOP))


def setupDungeon():
    global currMap, mapChanged
    currMap = dungeonMap
    mapChanged = dungeonMap


def spawnBoss():
    rand_x, rand_y = random.randrange(
        0, sight_block_column), random.randrange(0, sight_block_row)

    while(abs(player.x - rand_x) < 2.5 and abs(player.y - rand_y) < 2.5):
        rand_x = random.randrange(0, sight_block_column)
        rand_y = random.randrange(1, sight_block_row)

    boss_group.add(Boss(rand_x, rand_y, int(level / BOSS_INTERVAL)))
    staticEffect_group.add(
        StaticEffect(rand_x, rand_y, StaticEffect.TYPE_BOSS_SPAWN))


def coinFilter(amount):
    chest_content = []
    if amount / 50 > 0:
        for iter in range(int(amount / 50)):
            chest_content.append(ItemDrop.TYPE_COIN_50)
    amount %= 50
    if amount / 10 > 0:
        for iter in range(int(amount / 10)):
            chest_content.append(ItemDrop.TYPE_COIN_10)
    amount %= 10
    if amount / 5 > 0:
        for iter in range(int(amount / 5)):
            chest_content.append(ItemDrop.TYPE_COIN_5)
    amount %= 5
    if amount > 0:
        for iter in range(amount):
            chest_content.append(ItemDrop.TYPE_COIN_1)

    return chest_content


def chance(one_in_this_number):
    rand = random.randrange(1, one_in_this_number)
    return rand <= 1


def percentage(percent):
    rand = random.randrange(1, 100)
    return rand <= percent


RED = (200, 0, 0)
BLUE = (0, 0, 200)
GOLD = (225, 60, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PURPLE = (186, 85, 211)
GREEN = (0, 255, 0)

# Classes


class StatusCoin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 320
        self.y = 465
        self.image = img.coinImg_temp
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)


class Effect(pygame.sprite.Sprite):

    FONT_SIZE = 8
    DURATION = 25
    SPEED = 1

    FRAME_RATE = .4

    def __init__(self, x, y, type):
        super().__init__()
        self.x = x * pixel_per_block
        self.y = y * pixel_per_block
        self.type = type
        self.timer = 0

        if self.type == 'coin':
            self.image = img.coinImg
        elif self.type == 'heart':
            self.image = img.heartImg
        elif self.type == 'mana_potion':
            self.image = img.mana_potionImg_org
        elif self.type == 'broken_heart':
            self.image = img.broken_heartImg
        elif self.type == 'spark':
            self.sprites = img.spark_sprites
            self.currSprite = 0
            self.image = self.sprites[0]
        elif self.type == 'health_potion':
            self.image = img.health_potion_org
        elif self.type == 'boost':
            self.image = img.boostEffectImg

        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

    def update(self):
        self.y -= Effect.SPEED
        self.rect.topleft = (self.x, self.y)
        self.timer += 1
        # buffer_surface.blit(self.image, self.rect.topleft)

        if self.type == 'spark':
            self.currSprite += Effect.FRAME_RATE
            if self.currSprite >= len(self.sprites):
                self.currSprite = 0
            self.image = self.sprites[int(self.currSprite)]

        self.image.set_alpha(225 * (1 - self.timer / Effect.DURATION))

        if self.timer > Effect.DURATION:
            pygame.sprite.Sprite.remove(self, effect_group)


class TextDisplay(pygame.sprite.Sprite):

    BOUNCE_RANGE = .05
    MOVE_DIST = .005

    def __init__(self, x, y, text, font, color, duration=0, willDisappear=True, fadeOut=False, bounce=False):
        super().__init__()
        self.x = x
        self.y = y
        self.org_y = y
        self.duration = duration
        self.willDisapper = willDisappear
        self.fadeOut = fadeOut
        self.bounce = bounce
        if self.bounce:
            self.goDown = False
        self.timer = 0
        self.image = font.render(str(text), True, color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x * pixel_per_block,
                             self.y * pixel_per_block)

    def update(self):
        if self.willDisapper:
            self.timer += 1
            if self.fadeOut:
                self.image.set_alpha(255 * (1 - self.timer / self.duration))
            if self.timer >= self.duration:
                pygame.sprite.Sprite.remove(self, text_display_group)
        if self.bounce:
            upperBnd = self.org_y - TextDisplay.BOUNCE_RANGE
            lowerBnd = self.org_y + TextDisplay.BOUNCE_RANGE

            if upperBnd < self.y < lowerBnd:
                if self.goDown:
                    self.y += TextDisplay.MOVE_DIST
                else:
                    self.y -= TextDisplay.MOVE_DIST
            else:
                if self.y >= lowerBnd:
                    self.y -= TextDisplay.MOVE_DIST
                    self.goDown = False
                if self.y <= upperBnd:
                    self.y += TextDisplay.MOVE_DIST
                    self.goDown = True
            self.rect.topleft = (self.x * pixel_per_block,
                                 self.y * pixel_per_block)


class StaticEffect(pygame.sprite.Sprite):
    FRAME_RATE = .5

    TYPE_MOB_SPAWN = 0
    TYPE_BOSS_EXPLOSION = 1
    TYPE_BOSS_SPAWN = 2
    TYPE_SMOKE = 3

    def __init__(self, x, y, type=0):
        super().__init__()
        self.x = x
        self.y = y
        self.sprites = img.spawnEffect_sprites

        if type == StaticEffect.TYPE_BOSS_EXPLOSION:
            self.sprites = img.bossExplosion_sprites
        elif type == StaticEffect.TYPE_BOSS_SPAWN:
            self.sprites = img.bossSpawn_sprites
        elif type == StaticEffect.TYPE_SMOKE:
            self.sprites = img.smoke_sprites

        self.image = self.sprites[0]
        self.currSprite = 0
        self.rect = self.image.get_rect()
        self.rect.center = (self.x * pixel_per_block, self.y * pixel_per_block)

    def update(self):
        if self.currSprite >= len(self.sprites):
            pygame.sprite.Sprite.remove(self, staticEffect_group)
            return
        self.image = self.sprites[int(self.currSprite)]
        self.currSprite += StaticEffect.FRAME_RATE


class Mouse(pygame.sprite.Sprite):
    def __init__(self, image_source):
        super().__init__()
        self.image = image_source
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = pygame.mouse.get_pos()


class Block(pygame.sprite.Sprite):
    TYPE_BRICKS = 0

    TYPE_WOODEN_TOP_LEFT = 1
    TYPE_WOODEN_TOP_RIGHT = 2
    TYPE_WOODEN_BOTTOM_LEFT = 3
    TYPE_WOODEN_BOTTOM_RIGHT = 4
    TYPE_WOODEN_TOP = 5
    TYPE_WOODEN_BOTTOM = 6
    TYPE_WOODEN_LEFT = 7
    TYPE_WOODEN_RIGHT = 8
    TYPE_WOODEN_MIDDLE = 9

    TYPE_STONE_TOP_LEFT = 10
    TYPE_STONE_TOP_RIGHT = 11
    TYPE_STONE_BOTTOM_LEFT = 12
    TYPE_STONE_BOTTOM_RIGHT = 13
    TYPE_STONE_TOP = 14
    TYPE_STONE_BOTTOM = 15
    TYPE_STONE_LEFT = 16
    TYPE_STONE_RIGHT = 17
    TYPE_STONE_MIDDLE = 18

    TYPE_DUNGEON_WALL = 19
    TYPE_DUNGEON_WALL_SHADOW = 20
    TYPE_DUNGEON_TOP_LEFT = 21
    TYPE_DUNGEON_TOP_RIGHT = 22
    TYPE_DUNGEON_TOP = 23
    TYPE_DUNGEON_BOTTOM_LEFT = 24
    TYPE_DUNGEON_BOTTOM_RIGHT = 25
    TYPE_DUNGEON_BOTTOM = 26
    TYPE_DUNGEON_LEFT = 27
    TYPE_DUNGEON_RIGHT = 28
    TYPE_DUNGEON_MIDDLE = 29

    def __init__(self, type, x, y):
        super().__init__()
        self.type = type
        self.x = x
        self.y = y
        if type == Block.TYPE_BRICKS:
            self.image = img.bricks
        elif type == Block.TYPE_WOODEN_TOP_LEFT:
            self.image = img.wooden_floor_topleft
        elif type == Block.TYPE_WOODEN_TOP_RIGHT:
            self.image = img.wooden_floor_topright
        elif type == Block.TYPE_WOODEN_BOTTOM_LEFT:
            self.image = img.wooden_floor_bottomleft
        elif type == Block.TYPE_WOODEN_BOTTOM_RIGHT:
            self.image = img.wooden_floor_bottomright
        elif type == Block.TYPE_WOODEN_TOP:
            self.image = img.wooden_floor_top
        elif type == Block.TYPE_WOODEN_BOTTOM:
            self.image = img.wooden_floor_bottom
        elif type == Block.TYPE_WOODEN_LEFT:
            self.image = img.wooden_floor_left
        elif type == Block.TYPE_WOODEN_RIGHT:
            self.image = img.wooden_floor_right
        elif type == Block.TYPE_WOODEN_MIDDLE:
            self.image = img.wooden_floor_middle

        elif type == Block.TYPE_STONE_TOP_LEFT:
            self.image = img.stone_floor_topleft
        elif type == Block.TYPE_STONE_TOP_RIGHT:
            self.image = img.stone_floor_topright
        elif type == Block.TYPE_STONE_BOTTOM_LEFT:
            self.image = img.stone_floor_bottomleft
        elif type == Block.TYPE_STONE_BOTTOM_RIGHT:
            self.image = img.stone_floor_bottomright
        elif type == Block.TYPE_STONE_TOP:
            self.image = img.stone_floor_top
        elif type == Block.TYPE_STONE_BOTTOM:
            self.image = img.stone_floor_bottom
        elif type == Block.TYPE_STONE_LEFT:
            self.image = img.stone_floor_left
        elif type == Block.TYPE_STONE_RIGHT:
            self.image = img.stone_floor_right
        elif type == Block.TYPE_STONE_MIDDLE:
            self.image = img.stone_floor_middle

        elif type == Block.TYPE_DUNGEON_WALL:
            self.image = img.dungeon_floor_wall
        elif type == Block.TYPE_DUNGEON_WALL_SHADOW:
            self.image = img.dungeon_floor_wall_shadow
        elif type == Block.TYPE_DUNGEON_TOP_LEFT:
            self.image = img.dungeon_floor_topleft
        elif type == Block.TYPE_DUNGEON_TOP_RIGHT:
            self.image = img.dungeon_floor_topright
        elif type == Block.TYPE_DUNGEON_TOP:
            self.image = img.dungeon_floor_top
        elif type == Block.TYPE_DUNGEON_BOTTOM_LEFT:
            self.image = img.dungeon_floor_bottomleft
        elif type == Block.TYPE_DUNGEON_BOTTOM_RIGHT:
            self.image = img.dungeon_floor_bottomright
        elif type == Block.TYPE_DUNGEON_BOTTOM:
            self.image = img.dungeon_floor_bottom
        elif type == Block.TYPE_DUNGEON_LEFT:
            self.image = img.dungeon_floor_left
        elif type == Block.TYPE_DUNGEON_RIGHT:
            self.image = img.dungeon_floor_right
        elif type == Block.TYPE_DUNGEON_MIDDLE:
            self.image = img.dungeon_floor_middle

        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x * pixel_per_block,
                             self.y * pixel_per_block)

# Map(bg)


shopMap = []
for row in range(sight_block_row):
    temp_row = []
    for column in range(sight_block_column):
        if row == 0 and column == 0:
            temp_row.append(Block.TYPE_WOODEN_TOP_LEFT)
        elif row == 0 and column == sight_block_column - 1:
            temp_row.append(Block.TYPE_WOODEN_TOP_RIGHT)
        elif row == sight_block_row - 1 and column == 0:
            temp_row.append(Block.TYPE_WOODEN_BOTTOM_LEFT)
        elif row == sight_block_row - 1 and column == sight_block_column - 1:
            temp_row.append(Block.TYPE_WOODEN_BOTTOM_RIGHT)
        elif row == 0 and 0 < column < sight_block_column - 1:
            temp_row.append(Block.TYPE_WOODEN_TOP)
        elif row == sight_block_row - 1 and 0 < column < sight_block_column - 1:
            temp_row.append(Block.TYPE_WOODEN_BOTTOM)
        elif column == 0 and 0 < row < sight_block_row - 1:
            temp_row.append(Block.TYPE_WOODEN_LEFT)
        elif column == sight_block_column - 1 and 0 < row < sight_block_row - 1:
            temp_row.append(Block.TYPE_WOODEN_RIGHT)
        else:
            temp_row.append(Block.TYPE_WOODEN_MIDDLE)
    shopMap.append(temp_row)


safeHouseMap = []
for row in range(sight_block_row):
    temp_row = []
    for column in range(sight_block_column):
        if row == 0 and column == 0:
            temp_row.append(Block.TYPE_STONE_TOP_LEFT)
        elif row == 0 and column == sight_block_column - 1:
            temp_row.append(Block.TYPE_STONE_TOP_RIGHT)
        elif row == sight_block_row - 1 and column == 0:
            temp_row.append(Block.TYPE_STONE_BOTTOM_LEFT)
        elif row == sight_block_row - 1 and column == sight_block_column - 1:
            temp_row.append(Block.TYPE_STONE_BOTTOM_RIGHT)
        elif row == 0 and 0 < column < sight_block_column - 1:
            temp_row.append(Block.TYPE_STONE_TOP)
        elif row == sight_block_row - 1 and 0 < column < sight_block_column - 1:
            temp_row.append(Block.TYPE_STONE_BOTTOM)
        elif column == 0 and 0 < row < sight_block_row - 1:
            temp_row.append(Block.TYPE_STONE_LEFT)
        elif column == sight_block_column - 1 and 0 < row < sight_block_row - 1:
            temp_row.append(Block.TYPE_STONE_RIGHT)
        else:
            temp_row.append(Block.TYPE_STONE_MIDDLE)
    safeHouseMap.append(temp_row)


dungeonMap = []
for row in range(sight_block_row):
    temp_row = []
    for column in range(sight_block_column):
        if row == 0:
            temp_row.append(Block.TYPE_DUNGEON_WALL)
        elif row == 1:
            temp_row.append(Block.TYPE_DUNGEON_WALL_SHADOW)
        elif row == 2 and column == 0:
            temp_row.append(Block.TYPE_DUNGEON_TOP_LEFT)
        elif row == 2 and column == sight_block_column - 1:
            temp_row.append(Block.TYPE_DUNGEON_TOP_RIGHT)
        elif row == 2 and 0 < column < sight_block_column - 1:
            temp_row.append(Block.TYPE_DUNGEON_TOP)
        elif row == sight_block_row - 1 and column == 0:
            temp_row.append(Block.TYPE_DUNGEON_BOTTOM_LEFT)
        elif row == sight_block_row - 1 and column == sight_block_column - 1:
            temp_row.append(Block.TYPE_DUNGEON_BOTTOM_RIGHT)
        elif row == sight_block_row - 1 and 0 < column < sight_block_column - 1:
            temp_row.append(Block.TYPE_DUNGEON_BOTTOM)
        elif 0 < row < sight_block_row - 1 and column == 0:
            temp_row.append(Block.TYPE_DUNGEON_LEFT)
        elif 0 < row < sight_block_row - 1 and column == sight_block_column - 1:
            temp_row.append(Block.TYPE_DUNGEON_RIGHT)
        else:
            temp_row.append(Block.TYPE_DUNGEON_MIDDLE)
    dungeonMap.append(temp_row)

currMap = dungeonMap
mapChanged = True


class Potion(pygame.sprite.Sprite):

    HEALTH_POTION_GENERATE_RATE = 15  # %

    TYPE_MANA_POTION = 0
    TYPE_HEALTH_POTION = 1

    HEALTH_POTION_REGEN = 10
    MANA_POTION_REGEN = 5

    count = 0
    MAX_COUNT = 12
    FRAME_RATE = .25


class Item:
    TYPE_HEALTH_POTION = 0
    TYPE_MANA_POTION = 1
    TYPE_TIER_1_WAND = 2
    TYPE_TIER_2_WAND = 3
    TYPE_SKELETON_PET_SPAWN_EGG = 4
    TYPE_SPEEDUP_BOOST = 5
    # TYPE_MANA_POTION = 1
    # TYPE_MANA_POTION = 1
    # TYPE_MANA_POTION = 1
    TYPE_PET_CAKE = 6

    def __init__(self, type, count):
        self.type = type
        self.count = count


class Player(pygame.sprite.Sprite):

    SPEED = .06 * velocity_fix
    MANA_PER_POTION = 2
    STARTING_MANA = 0
    STARTING_HEALTH = 5

    AUTO_HEALTH_POTION_LINE = 50
    AUTO_MANA_POTION_LINE = 250

    MAX_MANA = 500

    def __init__(self, x, y):
        super().__init__()
        self.image = img.playerImg
        self.x = x
        self.y = y
        self.wand_level = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.inventory = [Item(Item.TYPE_HEALTH_POTION, 0),
                          Item(Item.TYPE_MANA_POTION, 0),
                          Item(Item.TYPE_TIER_1_WAND, 0),
                          Item(Item.TYPE_TIER_2_WAND, 0),
                          Item(Item.TYPE_SKELETON_PET_SPAWN_EGG, 0),
                          Item(Item.TYPE_SPEEDUP_BOOST, 0),
                          Item(Item.TYPE_PET_CAKE, 0)]

        self.health = Player.STARTING_HEALTH
        self.coin = 0
        # self.mana_potion = 0
        # self.health_potion = 0
        self.score = 0

        self.velocity_x = 0
        self.velocity_y = 0
        self.direction = 'left'
        self.idle = True
        self.shooting = False
        self.usingHealthPotion = False
        self.usingManaPotion = False
        self.autoHealthPotion = False
        self.autoManaPotion = False
        self.wand_tier = 0

        self.mana = Player.STARTING_MANA

        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x * pixel_per_block,
                             self.y * pixel_per_block)

    def update(self):
        if self.velocity_x != 0 or self.velocity_y != 0:
            staticEffect_group.add(StaticEffect(
                self.x + .5, self.y + 1, StaticEffect.TYPE_SMOKE))

        if self.health <= 0:
            pygame.sprite.Sprite.remove(self, player_group)
        elif self.health > 100:
            self.health = 100

        if self.mana > Player.MAX_MANA:
            self.mana = Player.MAX_MANA

        if self.velocity_y > 0:
            if self.y + self.velocity_y < sight_block_row - .8:
                self.y += self.velocity_y
            else:
                self.velocity_y = -self.velocity_y * .1

        if self.velocity_x > 0:
            self.direction = 'right'
            if self.x + self.velocity_x < sight_block_column - 1:
                self.x += self.velocity_x
            else:
                self.velocity_x = -self.velocity_x * .1

        if self.velocity_y < 0:
            if self.y + self.velocity_y > 0:
                self.y += self.velocity_y
            else:
                self.velocity_y = -self.velocity_y * .1

        if self.velocity_x < 0:
            self.direction = 'left'
            if self.x + self.velocity_x > 0:
                self.x += self.velocity_x
            else:
                self.velocity_x = -self.velocity_x * .1

        if self.direction == 'right':
            self.image = pygame.transform.flip(img.playerImg, True, False)
        else:
            self.image = img.playerImg

        self.rect.topleft = (self.x * pixel_per_block,
                             self.y * pixel_per_block)

        if self.velocity_x == 0:
            self.idle = True
        else:
            self.idle = False

        if self.idle:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            mouse_x /= pixel_per_block
            mouse_y /= pixel_per_block
            deltaX = mouse_x - self.x
            if deltaX > 0:
                self.direction = 'right'
            else:
                self.direction = 'left'


player = Player(7, 4)  # Put Player in the Middle of the Screen
player_group.add(player)


class Fireball(pygame.sprite.Sprite):

    FRAME_RATE = .25
    SPEED = .05 * velocity_fix
    EXPLOSION_DURATION = 20

    def __init__(self, start_x, start_y, end_x, end_y, degree):
        super().__init__()
        self.x = start_x
        self.y = start_y
        self.degree = degree
        self.timer = 0
        self.collided = False
        self.outOfBound = False

        self.deltaX = end_x - start_x
        self.deltaY = end_y - start_y
        self.base = (self.deltaX ** 2 + self.deltaY ** 2) ** .5

        self.sprites = []
        self.sprites.append(pygame.transform.rotate(
            img.fireball_sprites[0], self.degree))
        self.sprites.append(pygame.transform.rotate(
            img.fireball_sprites[1], self.degree))
        self.sprites.append(pygame.transform.rotate(
            img.fireball_sprites[2], self.degree))
        self.sprites.append(pygame.transform.rotate(
            img.fireball_sprites[3], self.degree))
        self.sprites.append(pygame.transform.rotate(
            img.fireball_sprites[4], self.degree))
        self.currSprite = 0

        self.explosion_sprites = []
        self.explosion_sprites.append(
            pygame.transform.rotate(img.explosionImg1, self.degree))
        self.explosion_sprites.append(
            pygame.transform.rotate(img.explosionImg2, self.degree))
        self.explosion_sprites.append(
            pygame.transform.rotate(img.explosionImg3, self.degree))

        self.image = self.sprites[0]
        self.rect = self.image.get_rect()

        self.rect.center = (self.x * pixel_per_block, self.y * pixel_per_block)

    def update(self):

        if pygame.sprite.spritecollide(self, slime_group, False) or pygame.sprite.spritecollide(self, boss_group, False):
            self.collided = True

        if (self.x > sight_block_column - .2 or self.x < .2 or self.y > sight_block_row - .2 or self.y < .2) and not self.outOfBound:
            self.outOfBound = True

        if self.outOfBound or self.collided:
            self.timer += 1
            self.currSprite += Fireball.FRAME_RATE
            if self.currSprite >= len(self.explosion_sprites):
                self.currSprite = 0
            self.image = self.explosion_sprites[int(self.currSprite)]
            # eliminate self from fireball_group if went out of boundaries
            if self.timer >= Fireball.EXPLOSION_DURATION:
                pygame.sprite.Sprite.remove(self, fireball_group)
        else:
            self.currSprite += self.FRAME_RATE
            if self.currSprite >= len(self.sprites):
                self.currSprite = 0

            self.image = self.sprites[int(self.currSprite)]

            velocity_x = (self.deltaX / self.base) * Fireball.SPEED
            velocity_y = (self.deltaY / self.base) * Fireball.SPEED

            self.x += velocity_x
            self.y += velocity_y

            self.rect.center = (self.x * pixel_per_block,
                                self.y * pixel_per_block)

    @staticmethod
    def generate():
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_x /= pixel_per_block
        mouse_y /= pixel_per_block
        start_x = player.x + .5
        start_y = player.y + .5
        deltaX = mouse_x - start_x
        deltaY = mouse_y - start_y
        base = (deltaX ** 2 + deltaY ** 2) ** .5

        sinD = deltaY / base
        cosD = deltaX / base

        if sinD * cosD == 0:  # on axis
            Degree = 0
        elif sinD * cosD > 0:  # in I or III
            if sinD > 0 and cosD > 0:  # I
                Degree = -((math.asin(sinD) / math.pi * 180) + 90)
            elif sinD < 0 and cosD < 0:  # III
                Degree = 90 - (math.asin(-sinD) / math.pi * 180)
        elif sinD * cosD < 0:  # in II or IV
            if sinD > 0 and cosD < 0:  # II
                Degree = (math.asin(sinD) / math.pi * 180) + 90
            if sinD < 0 and cosD > 0:  # IV
                Degree = -(90 - (math.asin(-sinD) / math.pi * 180))

        if deltaX == 0 and deltaY == 0:
            return
        fireball_group.add(
            Fireball(start_x, start_y, mouse_x, mouse_y, Degree))


class Electricball(pygame.sprite.Sprite):

    FRAME_RATE = 1
    SPEED = .5 * velocity_fix

    def __init__(self, start_x, start_y, end_x, end_y, degree):
        super().__init__()
        self.x = start_x
        self.y = start_y
        self.degree = degree
        self.collided = False
        self.outOfBound = False

        self.deltaX = end_x - start_x
        self.deltaY = end_y - start_y
        self.base = (self.deltaX ** 2 + self.deltaY ** 2) ** .5

        self.sprites = []

        for iter in range(len(img.electric_ball_sprites)):
            self.sprites.append(pygame.transform.rotate(
                img.electric_ball_sprites[iter], self.degree))

        self.currSprite = 0

        self.image = self.sprites[0]
        self.rect = self.image.get_rect()

        self.rect.center = (self.x * pixel_per_block, self.y * pixel_per_block)

    def update(self):

        if pygame.sprite.spritecollide(self, slime_group, False) or pygame.sprite.spritecollide(self, boss_group, False):
            self.collided = True

        if (self.x > sight_block_column - .2 or self.x < .2 or self.y > sight_block_row - .2 or self.y < .2) and not self.outOfBound:
            self.outOfBound = True

        if self.outOfBound or self.collided:
            pygame.sprite.Sprite.remove(self, electricball_group)
        else:
            self.currSprite += self.FRAME_RATE
            if self.currSprite >= len(self.sprites):
                self.currSprite = 0

            self.image = self.sprites[int(self.currSprite)]

            velocity_x = (self.deltaX / self.base) * Electricball.SPEED
            velocity_y = (self.deltaY / self.base) * Electricball.SPEED

            self.x += velocity_x
            self.y += velocity_y

            self.rect.center = (self.x * pixel_per_block,
                                self.y * pixel_per_block)

    @staticmethod
    def generate():
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_x /= pixel_per_block
        mouse_y /= pixel_per_block
        start_x = player.x + .5
        start_y = player.y + .5
        deltaX = mouse_x - start_x
        deltaY = mouse_y - start_y
        base = (deltaX ** 2 + deltaY ** 2) ** .5

        sinD = deltaY / base
        cosD = deltaX / base

        if sinD * cosD == 0:  # on axis
            Degree = 0
        elif sinD * cosD > 0:  # in I or III
            if sinD > 0 and cosD > 0:  # I
                Degree = -((math.asin(sinD) / math.pi * 180) + 90)
            elif sinD < 0 and cosD < 0:  # III
                Degree = 90 - (math.asin(-sinD) / math.pi * 180)
        elif sinD * cosD < 0:  # in II or IV
            if sinD > 0 and cosD < 0:  # II
                Degree = (math.asin(sinD) / math.pi * 180) + 90
            if sinD < 0 and cosD > 0:  # IV
                Degree = -(90 - (math.asin(-sinD) / math.pi * 180))

        # Degree = ((math.asin(sinD)) / math.pi) * 180 + 90
        # Degree = 90
        if deltaX == 0 and deltaY == 0:
            return

        electricball_group.add(Electricball(
            start_x, start_y, mouse_x, mouse_y, Degree))


class Slime(pygame.sprite.Sprite):

    MAX_COIN_DROP = 2
    SPEED = .012 * velocity_fix
    DAMAGE_PER_COLLISION = 10

    COIN_PER_KILL = 1
    SCORE_PER_KILL = 3
    STARTING_HEALTH = 15
    COIN_SCATTER_RANGE = .3
    POTION_DROP_RATE = 58  # 58%

    SPEEDUP_BOOST_DROP_RATE = 20000  # 1 in 20000
    TIER_1_WAND_DROP_RATE = 40000
    TIER_2_WAND_DROP_RATE = 80000

    def __del__(self):
        global currMob_count
        currMob_count -= 1

    def __init__(self, x, y):
        global currMob_count
        currMob_count += 1
        super().__init__()
        self.x = x
        self.y = y

        self.direction = 'left'
        self.health = Slime.STARTING_HEALTH
        self.collided = False

        self.image = img.slimeImg
        self.rect = self.image.get_rect()
        self.rect.center = (self.x * pixel_per_block, self.y * pixel_per_block)

    def update(self):
        if self.y < 1:
            self.y = 1

        deltaX = (player.x + .5) - self.x
        deltaY = (player.y + .5) - self.y

        base = (deltaX ** 2 + deltaY ** 2) ** .5

        velocity_x = (deltaX / base) * Slime.SPEED
        velocity_y = (deltaY / base) * Slime.SPEED

        if velocity_x > 0:
            self.direction = 'right'
        elif velocity_x < 0:
            self.direction = 'left'

        if self.direction == 'right':
            self.image = pygame.transform.flip(img.slimeImg, True, False)
        else:
            self.image = img.slimeImg

        self.x += velocity_x
        self.y += velocity_y

        self.rect.center = (self.x * pixel_per_block, self.y * pixel_per_block)
        fireball_group.update()

        if self.rect.colliderect(player.rect):
            player.health -= Slime.DAMAGE_PER_COLLISION / 2
            effect_group.add(Effect(
                player.x, player.y, 'broken_heart'))
            self.health = 0

        if pygame.sprite.spritecollide(self, fireball_group, False):
            self.collided = True
            self.health -= Wand.getDamageOfProjectile('fireball')

        if pygame.sprite.spritecollide(self, electricball_group, False):
            self.collided = True
            self.health -= Wand.getDamageOfProjectile('electricball')

        if self.health <= 0:
            if self.collided and level % BOSS_INTERVAL != 0:
                global kill_cnt
                player.score += Slime.SCORE_PER_KILL
                kill_cnt += 1
                chest_content = Slime.generateDrop()
                if len(chest_content) > 0:
                    item_drop_group.add(
                        ItemDrop(self.x, self.y, ItemDrop.TYPE_SMALL_WOODEN_CHEST, chest_content))

            pygame.sprite.Sprite.remove(self, slime_group)
            aud.slimeDeath.play()
            Slime.generateSlime()
            return

    @staticmethod
    def generateSlime():
        rand_x = random.randrange(0, sight_block_column)
        rand_y = random.randrange(1, sight_block_row)

        while(abs(player.x - rand_x) < 2 and abs(player.y - rand_y) < 2):
            rand_x = random.randrange(0, sight_block_column)
            rand_y = random.randrange(0, sight_block_row)

        slime_group.add(Slime(rand_x, rand_y))
        staticEffect_group.add(
            StaticEffect(rand_x, rand_y, StaticEffect.TYPE_MOB_SPAWN))

    @staticmethod
    def generateDrop():
        chest_content = coinFilter(random.randrange(0, Slime.MAX_COIN_DROP))
        if percentage(Slime.POTION_DROP_RATE):
            if percentage(Potion.HEALTH_POTION_GENERATE_RATE):
                chest_content.append(ItemDrop.TYPE_HEALTH_POTION)
            else:
                chest_content.append(ItemDrop.TYPE_MANA_POTION)
        if chance(Slime.SPEEDUP_BOOST_DROP_RATE):
            chest_content.append(ItemDrop.TYPE_SPEEDUP_BOOST)
        if chance(Slime.TIER_1_WAND_DROP_RATE):
            chest_content.append(ItemDrop.TYPE_WAND_TIER_1)
        if chance(Slime.TIER_2_WAND_DROP_RATE):
            chest_content.append(ItemDrop.TYPE_WAND_TIER_2)

        return chest_content


boss_list = []


class BossHealthBar(pygame.sprite.Sprite):

    def __init__(self, count):
        super().__init__()
        self.x = (boss_list[count - 1].x + .1)
        self.y = (boss_list[count - 1].y - .8)
        self.count = count

        self.sprites = img.healthBar_sprites
        self.image = self.sprites[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x * pixel_per_block,
                             self.y * pixel_per_block)

    def update(self):
        health = 100
        while health >= 0:
            if boss_list[self.count - 1].health >= Boss.STARTING_HEALTH * health * .01:
                self.image = self.sprites[int(
                    len(self.sprites) - health / 2.5 - 1)]
                break
            health -= 2.5

        if boss_list[self.count - 1].health <= 0:
            pygame.sprite.Sprite.remove(self, boss_health_bar_group)

        self.x = (boss_list[self.count - 1].x - .3)
        self.y = (boss_list[self.count - 1].y - .5)
        self.rect.topleft = ((self.x - .9) * pixel_per_block,
                             (self.y - .8) * pixel_per_block)


class Boss(pygame.sprite.Sprite):

    SPEED = .05 * velocity_fix
    DAMAGE_PER_COLLISION = 5
    COIN_PER_KILL = 50
    SCORE_PER_KILL = 150
    STARTING_HEALTH = 2400

    INCREASE_POTION_PER_COUNT = 16
    INCREASE_COIN_PER_COUNT = 200

    SPEED_UP_BOOST_DROP_RATE = 15  # 1 in 17

    TIER_1_WAND_DROP_RATE = 30
    TIER_2_WAND_DROP_RATE = 60

    def __init__(self, x, y, count):
        super().__init__()
        self.x = x
        self.y = y
        self.count = count
        self.health = Boss.STARTING_HEALTH

        self.direction = 'left'
        self.collided = False
        boss_list.append(self)
        boss_health_bar_group.add(BossHealthBar(self.count))

        self.image = img.bossImg
        self.rect = self.image.get_rect()
        self.rect.center = (self.x * pixel_per_block, self.y * pixel_per_block)

    def update(self):
        global screenShake
        screenShake = True
        boss_list[self.count - 1] = self

        if pygame.sprite.spritecollide(self, fireball_group, True):
            self.collided = True
            self.health -= Wand.getDamageOfProjectile('fireball')
        if pygame.sprite.spritecollide(self, electricball_group, False):
            self.collided = True
            self.health -= Wand.getDamageOfProjectile('electricball')

        # if self.collided:
        #     self.collided = False

        deltaX = (player.x + .5) - self.x
        deltaY = (player.y + .5) - self.y

        base = (deltaX ** 2 + deltaY ** 2) ** .5

        velocity_x = (deltaX / base) * Slime.SPEED
        velocity_y = (deltaY / base) * Slime.SPEED

        if velocity_x > 0:
            self.direction = 'right'
        elif velocity_x < 0:
            self.direction = 'left'

        if self.direction == 'right':
            self.image = img.bossImg
        else:
            self.image = pygame.transform.flip(img.bossImg, True, False)

        self.x += velocity_x
        self.y += velocity_y

        self.rect.center = (self.x * pixel_per_block, self.y * pixel_per_block)

        if self.rect.colliderect(player.rect):
            player.health -= Boss.DAMAGE_PER_COLLISION / 2
            effect_group.add(Effect(
                player.x, player.y, 'broken_heart'))

        if self.health <= 0:
            staticEffect_group.add(StaticEffect(
                self.x, self.y, StaticEffect.TYPE_BOSS_EXPLOSION))
            pygame.sprite.Sprite.remove(self, boss_group)

            player.coin += Boss.COIN_PER_KILL
            player.score += Boss.SCORE_PER_KILL
            effect_group.add(Effect(
                player.x - .5, player.y, 'coin'))

            Boss.generateDrop(self.count, self.x, self.y)
            global bossKilled
            bossKilled = True
            screenShake = False

    @staticmethod
    def generateDrop(count, x, y):
        # Drop coins
        chest_content = coinFilter(random.randrange(
            count * Boss.INCREASE_COIN_PER_COUNT / 2, count * Boss.INCREASE_COIN_PER_COUNT))
        # Drop Potions
        rand = random.randrange(
            0, count * Boss.INCREASE_POTION_PER_COUNT / 2)
        for iter in range(count * Boss.INCREASE_POTION_PER_COUNT - rand):
            chest_content.append(ItemDrop.TYPE_MANA_POTION)
        for iter in range(rand):
            chest_content.append(ItemDrop.TYPE_HEALTH_POTION)
        # Specified Drops
        if count == 1:
            chest_content.append(ItemDrop.TYPE_SPEEDUP_BOOST)
            item_drop_group.add(
                ItemDrop(x, y, ItemDrop.TYPE_SILVER_CHEST, chest_content))
        elif count == 2:
            chest_content.append(ItemDrop.TYPE_WAND_TIER_2)
            item_drop_group.add(
                ItemDrop(x, y, ItemDrop.TYPE_GOLDEN_CHEST, chest_content))
        else:
            # Drop Speedup Boost by chance
            if chance(Boss.SPEED_UP_BOOST_DROP_RATE):
                chest_content.append(ItemDrop.TYPE_SPEEDUP_BOOST)
            # Wand Drops
            if chance(Boss.TIER_1_WAND_DROP_RATE):
                chest_content.append(ItemDrop.TYPE_WAND_TIER_1)
            if chance(Boss.TIER_2_WAND_DROP_RATE):
                chest_content.append(ItemDrop.TYPE_WAND_TIER_2)
            # add Treasure Chest to item_drop_group
            item_drop_group.add(
                ItemDrop(x, y, ItemDrop.TYPE_WOODEN_CHEST, chest_content))


class PlayerHealthBar(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.x = 304 * velocity_fix
        self.y = 470 * velocity_fix

        self.sprites = img.healthBar_sprites
        self.image = self.sprites[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

    def update(self):

        health = 100
        while health >= 0:
            if player.health >= health:
                self.image = self.sprites[int(
                    len(self.sprites) - health / 2.5 - 1)]
                break
            health -= 2.5


class PlayerManaBar(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.x = 492 * velocity_fix
        self.y = 470 * velocity_fix

        self.sprites = img.manaBar_sprites
        self.image = self.sprites[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

    def update(self):
        mana = 100
        while mana >= 0:
            if player.mana >= mana * .01 * Player.MAX_MANA:
                self.image = self.sprites[int(
                    len(self.sprites) - mana / 2.5 - 1)]
                break
            mana -= 2.5


class Wand(pygame.sprite.Sprite):

    MAX_TIER = 2

    TIER1_DAMAGE = 20
    TIER2_DAMAGE = 45

    TIER1_DAMAGE_INCREASE_RATE = .25
    TIER2_DAMAGE_INCREASE_RATE = .3

    TIER1_MANA_COST = 1
    TIER2_MANA_COST = 2

    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0
        self.image = img.wand_1_Img
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def update(self):

        self.x = player.x + .1
        self.y = player.y + .8
        self.rect.center = (self.x * pixel_per_block, self.y * pixel_per_block)

        mouse_x, mouse_y = pygame.mouse.get_pos()
        deltaX = mouse_x / pixel_per_block - self.x
        deltaY = mouse_y / pixel_per_block - self.y
        base = (deltaX ** 2 + deltaY ** 2) ** .5

        sinD = deltaY / base
        cosD = deltaX / base

        if sinD * cosD == 0:  # on axis
            if sinD == 0 and cosD == 0:
                Degree = 0
            elif sinD == 0:
                Degree = -90
            elif cosD == 0:
                Degree = 0
        elif sinD * cosD > 0:  # in I or III
            if sinD > 0 and cosD > 0:  # I
                Degree = -((math.asin(sinD) / math.pi * 180) + 90)
            elif sinD < 0 and cosD < 0:  # III
                Degree = 90 - (math.asin(-sinD) / math.pi * 180)
        elif sinD * cosD < 0:  # in II or IV
            if sinD > 0 and cosD < 0:  # II
                Degree = (math.asin(sinD) / math.pi * 180) + 90
            if sinD < 0 and cosD > 0:  # IV
                Degree = -(90 - (math.asin(-sinD) / math.pi * 180))

        if player.wand_tier == 1:
            self.image = pygame.transform.rotate(img.wand_1_Img, Degree)
        elif player.wand_tier == 2:
            self.image = pygame.transform.rotate(img.wand_2_Img, Degree)

    @staticmethod
    def isWandUnlocked(tier):
        if player.wand_level[tier - 1] > 0:
            return True
        else:
            return False

    @staticmethod
    def getDamageOfProjectile(type):
        if type == 'fireball':
            return ((player.wand_level[0] - 1) * Wand.TIER1_DAMAGE_INCREASE_RATE + 1) * Wand.TIER1_DAMAGE
        elif type == 'electricball':
            return ((player.wand_level[0] - 1) * Wand.TIER2_DAMAGE_INCREASE_RATE + 1) * Wand.TIER2_DAMAGE


item_drop_on_scene = []


class ItemDrop(pygame.sprite.Sprite):

    SPARK_GENERATE_FRAME = 4
    SPARK_GENERATE_RANGE = .3
    FRAME_RATE = .25

    CHEST_OPEN_DURATION = 30
    SPEED_UP_BOOST_RATE = 1.08

    CHEST_ITEM_SCATTER_RANGE = .6

    TYPE_WOODEN_CHEST = 0
    TYPE_SILVER_CHEST = 1
    TYPE_GOLDEN_CHEST = 2
    TYPE_SPEEDUP_BOOST = 3
    TYPE_HEALTH_POTION = 4
    TYPE_MANA_POTION = 5
    TYPE_COIN_1 = 6
    TYPE_COIN_5 = 7
    TYPE_COIN_10 = 8
    TYPE_COIN_50 = 9
    TYPE_WAND_TIER_1 = 10
    TYPE_WAND_TIER_2 = 11
    TYPE_SMALL_WOODEN_CHEST = 12
    TYPE_SKELETON_PET_SPAWN_EGG = 13
    TYPE_PET_CAKE = 14

    def __init__(self, x, y, type, content=[]):
        super().__init__()
        item_drop_on_scene.append(self)
        self.x = x
        self.y = y
        self.type = type
        self.image = img.woodenChest_sprites[0]
        self.hasParticleEffect = False
        self.isContainer = False

        if self.type == ItemDrop.TYPE_WOODEN_CHEST:
            self.sprites = img.woodenChest_sprites
            self.image = self.sprites[0]
            self.content = content
            self.timer = 0
            self.opened = False
            self.hasParticleEffect = True
            self.isContainer = True
        elif self.type == ItemDrop.TYPE_SILVER_CHEST:
            self.sprites = img.silverChest_sprites
            self.image = self.sprites[0]
            self.content = content
            self.timer = 0
            self.opened = False
            self.hasParticleEffect = True
            self.isContainer = True
        elif self.type == ItemDrop.TYPE_GOLDEN_CHEST:
            self.sprites = img.goldenChest_sprites
            self.image = self.sprites[0]
            self.content = content
            self.timer = 0
            self.opened = False
            self.hasParticleEffect = True
            self.isContainer = True
        elif self.type == ItemDrop.TYPE_SPEEDUP_BOOST:
            self.image = img.speedupBoostImg
            self.hasParticleEffect = True
        elif self.type == ItemDrop.TYPE_HEALTH_POTION:
            self.sprites = img.health_potion_sprites
            self.image = self.sprites[0]
            self.currSprite = 0
        elif self.type == ItemDrop.TYPE_MANA_POTION:
            self.sprites = img.mana_potion_sprites
            self.image = self.sprites[0]
            self.currSprite = 0
        elif self.type == ItemDrop.TYPE_COIN_1:
            self.image = img.item_coinImg
        elif self.type == ItemDrop.TYPE_COIN_5:
            self.image = pygame.transform.scale(img.item_coinImg, (20, 20))
        elif self.type == ItemDrop.TYPE_COIN_10:
            self.image = pygame.transform.scale(img.item_coinImg, (24, 24))
        elif self.type == ItemDrop.TYPE_COIN_50:
            self.image = pygame.transform.scale(img.item_coinImg, (32, 32))
        elif self.type == ItemDrop.TYPE_WAND_TIER_1:
            self.image = pygame.transform.rotate(img.wand_1_Img, 75)
            self.hasParticleEffect = True
        elif self.type == ItemDrop.TYPE_WAND_TIER_2:
            self.image = pygame.transform.rotate(img.wand_2_Img, 75)
            self.hasParticleEffect = True
        elif self.type == ItemDrop.TYPE_SMALL_WOODEN_CHEST:
            self.sprites = img.small_woodenChest_sprites
            self.image = self.sprites[0]
            self.content = content
            self.timer = 0
            self.opened = False
            self.isContainer = True
        elif self.type == ItemDrop.TYPE_SKELETON_PET_SPAWN_EGG:
            self.image = img.gold_spawn_egg
            self.hasParticleEffect = True
        elif self.type == ItemDrop.TYPE_PET_CAKE:
            self.image = img.petCake
            self.hasParticleEffect = True
        self.rect = self.image.get_rect()
        self.rect.center = (self.x * pixel_per_block, self.y * pixel_per_block)

    def update(self):
        if self.x < 0:
            self.x = 0
        if self.y < 1:
            self.y = 1
        if self.x > sight_block_column:
            self.x = sight_block_column
        if self.y > sight_block_row:
            self.y = sight_block_row
        if self.rect.center != (self.x * pixel_per_block, self.y * pixel_per_block):
            self.rect.center = (self.x * pixel_per_block,
                                self.y * pixel_per_block)

        if self.type == ItemDrop.TYPE_PET_CAKE:
            if pygame.sprite.spritecollide(self, skeleton_pet_group, False):
                effect_group.add(Effect(self.x, self.y, 'boost'))
                SkeletonPet.SPEED *= 1.08

        if self.rect.colliderect(player.rect) or pygame.sprite.spritecollide(self, skeleton_pet_group, False):
            global inventoryChanged
            inventoryChanged = True
            if self.isContainer:
                if not self.opened:
                    self.opened = True
                    self.image = self.sprites[1]
                    aud.openChestSound.play()
            elif self.type == ItemDrop.TYPE_SPEEDUP_BOOST:
                pygame.sprite.Sprite.remove(self, item_drop_group)
                player.inventory[Item.TYPE_SPEEDUP_BOOST].count += 1
            elif self.type == ItemDrop.TYPE_HEALTH_POTION:
                # player.health_potion += 1
                pygame.sprite.Sprite.remove(self, item_drop_group)
                effect_group.add(Effect(self.x, self.y, 'health_potion'))
                aud.pickPotionSound.play()
                player.inventory[Item.TYPE_HEALTH_POTION].count += 1
            elif self.type == ItemDrop.TYPE_MANA_POTION:
                # player.mana_potion += 1
                pygame.sprite.Sprite.remove(self, item_drop_group)
                effect_group.add(Effect(self.x, self.y, 'mana_potion'))
                aud.pickPotionSound.play()
                player.inventory[Item.TYPE_MANA_POTION].count += 1
            elif self.type == ItemDrop.TYPE_COIN_1:
                player.coin += 1
                pygame.sprite.Sprite.remove(self, item_drop_group)
                effect_group.add(Effect(self.x, self.y, 'coin'))
                aud.pickCoinSound.play()
            elif self.type == ItemDrop.TYPE_COIN_5:
                player.coin += 5
                pygame.sprite.Sprite.remove(self, item_drop_group)
                effect_group.add(Effect(self.x, self.y, 'coin'))
                aud.pickCoinSound.play()
            elif self.type == ItemDrop.TYPE_COIN_10:
                player.coin += 10
                pygame.sprite.Sprite.remove(self, item_drop_group)
                effect_group.add(Effect(self.x, self.y, 'coin'))
                aud.pickCoinSound.play()
            elif self.type == ItemDrop.TYPE_COIN_50:
                player.coin += 50
                pygame.sprite.Sprite.remove(self, item_drop_group)
                effect_group.add(Effect(self.x, self.y, 'coin'))
                aud.pickCoinSound.play()
            elif self.type == ItemDrop.TYPE_WAND_TIER_1:
                pygame.sprite.Sprite.remove(self, item_drop_group)
                aud.pickItemSound.play()
                if player.wand_level[0] == 0:
                    global GameStart, counter, display_toolBar
                    display_toolBar = True
                    GameStart = True
                    # Wand.TIER_1_UNLOCKED = True
                    wand_group.add(Wand())
                    player.wand_tier = 1
                    for iter in range(MOB_COUNT):
                        Slime.generateSlime()
                    counter = 0
                player.wand_level[0] += 1
                player.inventory[Item.TYPE_TIER_1_WAND].count += 1
            elif self.type == ItemDrop.TYPE_WAND_TIER_2:
                pygame.sprite.Sprite.remove(self, item_drop_group)
                player.wand_level[1] += 1
                Wand.TIER_2_UNLOCKED = True
                aud.pickItemSound.play()
                player.inventory[Item.TYPE_TIER_2_WAND].count += 1
            elif self.type == ItemDrop.TYPE_SKELETON_PET_SPAWN_EGG:
                aud.eggCrack.play()
                pygame.sprite.Sprite.remove(self, item_drop_group)
                player.inventory[Item.TYPE_SKELETON_PET_SPAWN_EGG].count += 1
            elif self.type == ItemDrop.TYPE_PET_CAKE:
                pygame.sprite.Sprite.remove(self, item_drop_group)
                if self.rect.colliderect(player.rect):
                    player.inventory[Item.TYPE_PET_CAKE].count += 1

        else:  # before collide with player
            if (self.type == ItemDrop.TYPE_HEALTH_POTION) or (self.type == ItemDrop.TYPE_MANA_POTION):
                self.currSprite += ItemDrop.FRAME_RATE
                if self.currSprite >= len(self.sprites):
                    self.currSprite = 0
                self.image = self.sprites[int(self.currSprite)]

            # Only chests and speedup boosts have particle effects, so the fps wouldnt be affected too badly
            if self.hasParticleEffect:
                rand_x = random.randrange(
                    (int(self.x - ItemDrop.SPARK_GENERATE_RANGE + .25) * 10), int((self.x + ItemDrop.SPARK_GENERATE_RANGE + .25) * 10))
                rand_y = random.randrange(
                    int((self.y - ItemDrop.SPARK_GENERATE_RANGE) * 10), int((self.y + ItemDrop.SPARK_GENERATE_RANGE) * 10))
                rand_x /= 10
                rand_y /= 10
                effect_group.add(Effect(rand_x, rand_y, 'spark'))
                aud.bling.play()

        if self.isContainer:
            if self.opened == True:
                self.timer += 1
                if self.timer >= ItemDrop.CHEST_OPEN_DURATION:
                    for item_type in self.content:
                        rand_x = random.randrange(
                            -ItemDrop.CHEST_ITEM_SCATTER_RANGE * 10, ItemDrop.CHEST_ITEM_SCATTER_RANGE * 10)
                        rand_y = random.randrange(
                            -ItemDrop.CHEST_ITEM_SCATTER_RANGE * 10, ItemDrop.CHEST_ITEM_SCATTER_RANGE * 10)
                        rand_x /= 10
                        rand_y /= 10
                        item_drop_group.add(
                            ItemDrop(self.x + rand_x, self.y + rand_y, item_type))
                    pygame.sprite.Sprite.remove(self, item_drop_group)


class NPC(pygame.sprite.Sprite):

    TYPE_TUTOR = 0
    TYPE_SILVER_GUARD = 1
    TYPE_GOLDEN_GUARD = 2
    TYPE_SELLER = 3

    def __init__(self, x, y, type):
        super().__init__()
        self.x = x
        self.y = y
        self.type = type
        if self.type == NPC.TYPE_TUTOR:
            self.image = pygame.transform.flip(img.tutor, True, False)
            self.timer = 0
            self.collided = False
            text_display_group.add(TextDisplay(
                self.x - .2, self.y - 1, '!!!!!!', tutorialFont, WHITE, 0, False, False, True))
        if self.type == NPC.TYPE_SILVER_GUARD:
            self.image = img.silver_guard
            self.collided = False
            self.wasCollided = False
        if self.type == NPC.TYPE_GOLDEN_GUARD:
            self.image = img.golden_guard
            self.collided = False
            self.wasCollided = False

        self.rect = self.image.get_rect()
        self.rect.center = (self.x * pixel_per_block,
                            self.y * pixel_per_block)

    def update(self):
        if pygame.sprite.spritecollide(self, player_group, False):
            self.collided = True
        if self.collided:
            NPC.respond(self)

    def respond(NPC_obj):
        if NPC_obj.type == NPC.TYPE_TUTOR:
            if NPC_obj.timer == 0:
                text_display_group.empty()
                aud.tutorSpeak.play()
                text_display_group.add(TextDisplay(
                    NPC_obj.x - 1.5, NPC_obj.y - 1, 'Eggie, It\'s time for me to leave', tutorialFont, WHITE, 600, True, True, False))
            elif NPC_obj.timer == 650:
                aud.tutorSpeak.play()
            elif NPC_obj.timer == 750:
                text_display_group.add(TextDisplay(
                    NPC_obj.x - 1, NPC_obj.y - 1, 'You must embark alone...', tutorialFont, WHITE, 400, True, True, False))
            elif NPC_obj.timer == 1200:
                text_display_group.add(TextDisplay(
                    NPC_obj.x - 1, NPC_obj.y - 1, 'See you the other side...', tutorialFont, WHITE, 600, True, True, False))
            elif NPC_obj.timer == 1300:
                aud.dying.play()
            elif 1600 < NPC_obj.timer < 2100:
                NPC_obj.image.set_alpha(
                    255 * (1 - ((NPC_obj.timer - 1600) / 500)))
            elif NPC_obj.timer == 2100:
                NPC_obj.image.set_alpha(255)
                # aud.ah.play()
            elif NPC_obj.timer == 2150:
                aud.tutorSpeak.play()
                text_display_group.add(TextDisplay(
                    NPC_obj.x - .8, NPC_obj.y - 1, 'Ah... Here, take these...', tutorialFont, WHITE, 650, True, True, False))
            elif NPC_obj.timer == 2900:
                aud.dying.play()
            elif 2900 < NPC_obj.timer < 3400:
                NPC_obj.image.set_alpha(
                    255 * (1 - ((NPC_obj.timer - 2900) / 500)))
            elif NPC_obj.timer >= 3400:
                starting_chest_content = []
                for iter in range(15):
                    starting_chest_content.append(
                        ItemDrop.TYPE_HEALTH_POTION)
                for iter in range(20):
                    starting_chest_content.append(
                        ItemDrop.TYPE_MANA_POTION)
                starting_chest_content.append(ItemDrop.TYPE_WAND_TIER_1)
                item_drop_group.add(
                    ItemDrop(NPC_obj.x, NPC_obj.y, ItemDrop.TYPE_WOODEN_CHEST, starting_chest_content))
                npc_group.empty()

            NPC_obj.timer += 1


class StaticInstance(pygame.sprite.Sprite):

    TYPE_SHOP_MYSTERY_CHEST = 0
    TYPE_SHOP_HEALTH_POTION_CHEST = 1
    TYPE_SHOP_MANA_POTION_CHEST = 2

    MYSTERY_CHEST_PRICE = 3000
    HEALTH_POTION_CHEST_PRICE = 1500
    MANA_POTION_CHEST_PRICE = 1200

    MYSTERY_CHEST_SPEEDUP_BOOST_DROP_RATE = 3
    MYSTERY_CHEST_SKELETON_PET_DROP_RATE = 2
    MYSTERY_CHEST_PET_CAKE_DROP_RATE = 15

    def __init__(self, x, y, type, image_surf=None):
        super().__init__()
        self.x = x
        self.y = y
        self.type = type
        if self.type == StaticInstance.TYPE_SHOP_MYSTERY_CHEST:
            self.sprites = img.goldenChest_sprites
            self.image = self.sprites[0]
            text_display_group.add(TextDisplay(
                self.x - .78, self.y - .67, 'Mystery Chest', portalFont, WHITE, 0, False, False, True))
        elif self.type == StaticInstance.TYPE_SHOP_MANA_POTION_CHEST:
            self.sprites = img.woodenChest_sprites
            self.image = self.sprites[0]
            text_display_group.add(TextDisplay(
                self.x - 1.08, self.y - .67, 'Mana Potion Chest', portalFont, WHITE, 0, False, False, True))
        elif self.type == StaticInstance.TYPE_SHOP_HEALTH_POTION_CHEST:
            self.sprites = img.woodenChest_sprites
            self.image = self.sprites[0]
            text_display_group.add(TextDisplay(
                self.x - 1.1, self.y - .67, 'Health Potion Chest', portalFont, WHITE, 0, False, False, True))
        else:
            self.image = image_surf
        self.rect = self.image.get_rect()
        self.rect.center = (self.x * pixel_per_block,
                            self.y * pixel_per_block)

    def update(self):
        if pygame.sprite.spritecollide(self, player_group, False):
            if self.type == StaticInstance.TYPE_SHOP_MYSTERY_CHEST:
                self.image = self.sprites[1]
                aud.openChestSound.play()
                StaticInstance.displayInfo(img.mysteryChestInfoImg)
                buy = StaticInstance.confirmBuy()
                if buy and player.coin >= StaticInstance.MYSTERY_CHEST_PRICE:
                    player.coin -= StaticInstance.MYSTERY_CHEST_PRICE
                    item_drop_group.add(ItemDrop(
                        self.x, self.y + 2, ItemDrop.TYPE_GOLDEN_CHEST, StaticInstance.generateMysteryChestContent()))
                else:
                    aud.abortSound.play()
                player.x = self.x
                player.y = self.y + 3
                player.velocity_x = 0
                player.velocity_y = 0
                self.image = self.sprites[0]
            elif self.type == StaticInstance.TYPE_SHOP_HEALTH_POTION_CHEST:
                self.image = self.sprites[1]
                aud.openChestSound.play()
                StaticInstance.displayInfo(img.healthPotionChestInfoImg)
                buy = StaticInstance.confirmBuy()
                if buy and player.coin >= StaticInstance.HEALTH_POTION_CHEST_PRICE:
                    player.coin -= StaticInstance.HEALTH_POTION_CHEST_PRICE
                    item_drop_group.add(ItemDrop(
                        self.x, self.y + 2, ItemDrop.TYPE_WOODEN_CHEST, StaticInstance.generateHealthPotionChestContent()))
                else:
                    aud.abortSound.play()
                player.x = self.x
                player.y = self.y + 3
                player.velocity_x = 0
                player.velocity_y = 0
                self.image = self.sprites[0]
            elif self.type == StaticInstance.TYPE_SHOP_MANA_POTION_CHEST:
                self.image = self.sprites[1]
                aud.openChestSound.play()
                StaticInstance.displayInfo(img.manaPotionChestInfoImg)
                buy = StaticInstance.confirmBuy()
                if buy and player.coin >= StaticInstance.MANA_POTION_CHEST_PRICE:
                    player.coin -= StaticInstance.MANA_POTION_CHEST_PRICE
                    item_drop_group.add(ItemDrop(
                        self.x, self.y + 2, ItemDrop.TYPE_WOODEN_CHEST, StaticInstance.generateManaPotionChestContent()))
                else:
                    aud.abortSound.play()
                player.x = self.x
                player.y = self.y + 3
                player.velocity_x = 0
                player.velocity_y = 0
                self.image = self.sprites[0]

    @staticmethod
    def displayInfo(image_surf):
        info_window = image_surf
        screen.blit(info_window, (80, 88))
        pygame.display.update()
        spacePressed = False
        while not spacePressed:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    spacePressed = True

    @staticmethod
    def confirmBuy():
        keyPressed = False
        buy = True
        timer = 0
        CHANGE_SPRITE = 15
        confirm_window = random.choice(img.buyConfirm_sprites)
        while not keyPressed:
            timer += 1
            if timer >= CHANGE_SPRITE:
                confirm_window = random.choice(img.buyConfirm_sprites)
                timer = 0
            screen.blit(confirm_window, (280, 208))
            pygame.display.update()
            # waiting for keydown
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        buy = True
                        keyPressed = True
                    elif event.key == pygame.K_n:
                        buy = False
                        keyPressed = True
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        if keyPressed:
            return buy

    @staticmethod
    def generateMysteryChestContent():
        chest_content = []
        for iter in range(random.choice(range(6, 10))):
            chest_content.append(ItemDrop.TYPE_HEALTH_POTION)
        for iter in range(random.choice(range(6, 10))):
            chest_content.append(ItemDrop.TYPE_MANA_POTION)
        if percentage(StaticInstance.MYSTERY_CHEST_SPEEDUP_BOOST_DROP_RATE):
            chest_content.append(ItemDrop.TYPE_SPEEDUP_BOOST)
        if percentage(StaticInstance.MYSTERY_CHEST_SKELETON_PET_DROP_RATE):
            chest_content.append(ItemDrop.TYPE_SKELETON_PET_SPAWN_EGG)
        if percentage(StaticInstance.MYSTERY_CHEST_PET_CAKE_DROP_RATE):
            chest_content.append(ItemDrop.TYPE_PET_CAKE)

        return chest_content

    @staticmethod
    def generateHealthPotionChestContent():
        chest_content = []
        for iter in range(30):
            chest_content.append(ItemDrop.TYPE_HEALTH_POTION)
        return chest_content

    @staticmethod
    def generateManaPotionChestContent():
        chest_content = []
        for iter in range(30):
            chest_content.append(ItemDrop.TYPE_MANA_POTION)
        return chest_content


class Portal(pygame.sprite.Sprite):

    FRAME_RATE = .2

    USAGE_START_GAME = 0
    USAGE_NEXT_LEVEL = 1
    USAGE_SHOP = 2
    USAGE_BACK_FROM_SHOP = 3
    USAGE_SWEEP = 4
    USAGE_SAFE_HOUSE = 5
    USAGE_HOME = 6

    TYPE_GREEN_PORTAL = 0
    TYPE_PURPLE_PORTAL = 1

    IDLE_SOUND_INTERVAL = 25

    def __init__(self, x, y, dest_x, dest_y, type, usage):
        super().__init__()
        self.x = x
        self.y = y
        self.dest_x = dest_x
        self.dest_y = dest_y
        self.opened = False
        self.collided = False
        self.usage = usage
        self.currSprite = 0
        self.timer = 0
        if type == Portal.TYPE_GREEN_PORTAL:
            self.idle_sprites = img.green_portal_idle_sprites
            self.open_sprites = img.green_portal_open_sprites
            self.close_sprites = img.green_portal_close_sprites
        elif type == Portal.TYPE_PURPLE_PORTAL:
            self.idle_sprites = img.purple_portal_idle_sprites
            self.open_sprites = img.purple_portal_open_sprites
            self.close_sprites = img.purple_portal_close_sprites
        if self.usage == Portal.USAGE_NEXT_LEVEL:
            text_display_group.add(TextDisplay(
                self.x - .55, self.y - 1, 'Next Level', portalFont, WHITE, 0, False, False, True))
        elif self.usage == Portal.USAGE_BACK_FROM_SHOP:
            text_display_group.add(TextDisplay(
                self.x - .3, self.y - 1, 'Back', portalFont, GREEN, 0, False, False, True))
        elif self.usage == Portal.USAGE_SHOP:
            text_display_group.add(TextDisplay(
                self.x - .3, self.y - 1, 'Shop', portalFont, WHITE, 0, False, False, True))
        elif self.usage == Portal.USAGE_START_GAME:
            text_display_group.add(TextDisplay(
                self.x - .35, self.y - 1, 'Let\'s Go', portalFont, WHITE, 0, False, False, True))
        elif self.usage == Portal.USAGE_SAFE_HOUSE:
            text_display_group.add(TextDisplay(
                self.x - .63, self.y - 1, 'Safe House', portalFont, WHITE, 0, False, False, True))
        elif self.usage == Portal.USAGE_SWEEP:
            text_display_group.add(TextDisplay(
                self.x - .36, self.y - 1, 'Sweep', portalFont, WHITE, 0, False, False, True))
        self.image = self.idle_sprites[0]
        self.rect = self.image.get_rect()
        self.rect.center = (self.x * pixel_per_block,
                            self.y * pixel_per_block)

    def update(self):
        if pygame.sprite.spritecollide(self, player_group, False) and not self.collided:
            self.collided = True
            self.currSprite = 0

        if not self.opened:  # open
            self.currSprite += Portal.FRAME_RATE
            if self.currSprite >= len(self.open_sprites):
                self.opened = True
                self.currSprite = 0
                return
            self.image = self.open_sprites[int(self.currSprite)]
        elif self.collided:  # close
            self.currSprite += Portal.FRAME_RATE
            if self.currSprite >= len(self.close_sprites):
                if self.usage != Portal.USAGE_SWEEP:
                    teleport = Portal.confirmTeleport()
                    if teleport:
                        pygame.sprite.Sprite.remove(self, portal_group)
                        player.x = self.dest_x
                        player.y = self.dest_y
                        Portal.setGame(self.usage)
                        aud.teleportSoundd.play()
                        return
                    else:
                        self.collided = False
                        self.currSprite = 0
                        self.opened = False
                        player.x = 5
                        player.y = 5
                        player.velocity_y = 0
                        player.velocity_x = 0
                        aud.abortSound.play()
                        return
                else:
                    if level % BOSS_INTERVAL == 0:
                        player.x = self.dest_x
                        player.y = self.dest_y
                        aud.abortSound.play()
                        portal_group.empty()
                        text_display_group.empty()
                        static_instance_group.empty()
                        setupSafeHouse()
                        pygame.sprite.Sprite.remove(self, portal_group)
                        return
                    else:
                        teleport = Portal.confirmTeleport()
                        if teleport:
                            pygame.sprite.Sprite.remove(self, portal_group)
                            player.x = self.dest_x
                            player.y = self.dest_y
                            Portal.setGame(self.usage)
                            aud.teleportSoundd.play()
                            return
                        else:
                            self.collided = False
                            self.currSprite = 0
                            self.opened = False
                            player.x = 5
                            player.y = 5
                            player.velocity_y = 0
                            player.velocity_x = 0
                            aud.abortSound.play()
                            return
            self.image = self.close_sprites[int(self.currSprite)]
        else:  # idle
            self.timer += 1
            self.currSprite += Portal.FRAME_RATE
            if self.currSprite >= len(self.idle_sprites):
                self.currSprite = 0
            self.image = self.idle_sprites[int(self.currSprite)]
            if self.timer >= Portal.IDLE_SOUND_INTERVAL:
                aud.portalIdleSound.play()
                self.timer = 0

    @staticmethod
    def setGame(usage):
        global GameRest, levelCleared, level, updated
        portal_group.empty()
        text_display_group.empty()
        item_drop_group.empty()
        if usage == Portal.USAGE_START_GAME:
            npc_group.add(NPC(
                12, 4.5, NPC.TYPE_TUTOR))
        elif usage == Portal.USAGE_SHOP:
            setupShop()
        elif usage == Portal.USAGE_BACK_FROM_SHOP:
            static_instance_group.empty()
            setupSafeHouse()
        elif usage == Portal.USAGE_SAFE_HOUSE:
            setupSafeHouse()
        elif usage == Portal.USAGE_NEXT_LEVEL:
            setupDungeon()
            if levelCleared:
                GameRest = False
                levelCleared = False
                updated = False
                level += 1
                if level % BOSS_INTERVAL != 0:
                    text_display_group.add(TextDisplay(
                        4.9, 3, 'Level ' + str(level), clearLevelFont, WHITE, 100, True, True, False))
                    Slime.generateSlime()
                else:
                    text_display_group.add(TextDisplay(
                        3.1, 3, 'Boss Level', clearLevelFont, WHITE, 100, True, True, False))
            else:
                pass
        elif usage == Portal.USAGE_SWEEP:
            setupDungeon()
            GameRest = False
            levelCleared = False
            updated = False
            if level % BOSS_INTERVAL != 0:
                text_display_group.add(TextDisplay(
                    4.9, 3, 'Level ' + str(level), clearLevelFont, WHITE, 100, True, True, False))
                Slime.generateSlime()
            else:
                text_display_group.add(TextDisplay(
                    3.1, 3, 'Boss Level', clearLevelFont, WHITE, 100, True, True, False))

    @staticmethod
    def confirmTeleport():
        keyPressed = False
        teleport = True
        timer = 0
        CHANGE_SPRITE = 15
        confirm_window = random.choice(img.teleportConfirm_sprites)
        while not keyPressed:
            timer += 1
            if timer >= CHANGE_SPRITE:
                confirm_window = random.choice(img.teleportConfirm_sprites)
                timer = 0
            screen.blit(confirm_window, (280, 208))
            pygame.display.update()
            # waiting for keydown
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        teleport = True
                        keyPressed = True
                    elif event.key == pygame.K_n:
                        teleport = False
                        keyPressed = True
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        if keyPressed:
            return teleport


class SkeletonPet(pygame.sprite.Sprite):
    FRAME_RATE = .03
    SPEED = .02 * velocity_fix
    TYPE_SKELETON = 0

    STAY_DISTACNE = .5
    PICK_INTERVAL = 40
    CHANGE_STAY_SIDE = 800

    MAX_PICK_DURATION = 800

    def __init__(self, x, y, type):
        super().__init__()
        self.x = x
        self.y = y
        self.velocity_x = 0
        self.velocity_y = 0
        self.type = type
        self.timer = 0
        self.idle = True
        self.dest_x = 0
        self.dest_y = 0
        self.speed = SkeletonPet.SPEED
        self.destPicked = False
        self.facingRight = True
        self.stayRight = True

        if self.type == SkeletonPet.TYPE_SKELETON:
            self.idle_sprites = img.skeleton_idle_sprites
            self.run_sprites = img.skeleton_run_sprites
            self.image = self.idle_sprites[0]
            self.currSprite = 0

        self.rect = self.image.get_rect()
        self.rect.center = (self.x * pixel_per_block, self.y * pixel_per_block)

    def update(self):
        self.currSprite += SkeletonPet.FRAME_RATE
        self.timer += 1

        self.x += self.velocity_x
        self.y += self.velocity_y

        if self.x < .1:
            self.x = .1
        elif self.x > sight_block_column - .1:
            self.x = sight_block_column - .1
        if self.y < 1:
            self.y = 1
        elif self.y > sight_block_row - .1:
            self.y = sight_block_row - .1

        if self.velocity_x != 0:
            self.facingRight = (self.velocity_x > 0)

        self.idle = (self.velocity_x == 0) and (self.velocity_y == 0)
        if self.idle:
            if self.currSprite >= len(self.idle_sprites):
                self.currSprite = 0
            if self.facingRight:
                self.image = self.idle_sprites[int(self.currSprite)]
            else:
                self.image = pygame.transform.flip(
                    self.idle_sprites[int(self.currSprite)], True, False)
        else:
            if self.currSprite >= len(self.run_sprites):
                self.currSprite = 0
            if self.facingRight:
                self.image = self.run_sprites[int(self.currSprite)]
            else:
                self.image = pygame.transform.flip(
                    self.run_sprites[int(self.currSprite)], True, False)

        if not self.destPicked:
            if len(item_drop_group.sprites()) > 0:
                shortest_dist = 100
                item_picked = None
                for item in item_drop_group.sprites():
                    if getBase(item.x - self.x, item.y - self.y) < shortest_dist:
                        item_picked = item
                        shortest_dist = getBase(
                            item.x - self.x, item.y - self.y)
                self.dest_x = item_picked.x
                self.dest_y = item_picked.y
                self.destPicked = True
            else:
                if self.timer >= SkeletonPet.CHANGE_STAY_SIDE:
                    self.stayRight = not self.stayRight
                    self.timer = 0
                if self.stayRight:
                    if abs(player.x + .8 - self.x) > .05 or abs(player.y + .8 - self.y) > .05:
                        deltaX = (player.x + .8) - self.x
                        deltaY = (player.y + .8) - self.y
                        base = getBase(deltaX, deltaY)
                        self.velocity_x = (deltaX / base) * SkeletonPet.SPEED
                        self.velocity_y = (deltaY / base) * SkeletonPet.SPEED
                    else:
                        self.velocity_x = 0
                        self.velocity_y = 0
                else:
                    if abs(player.x - .3 - self.x) > .05 or abs(player.y + .8 - self.y) > .05:
                        deltaX = (player.x - .3) - self.x
                        deltaY = (player.y + .8) - self.y
                        base = getBase(deltaX, deltaY)
                        self.velocity_x = (deltaX / base) * SkeletonPet.SPEED
                        self.velocity_y = (deltaY / base) * SkeletonPet.SPEED
                    else:
                        self.velocity_x = 0
                        self.velocity_y = 0
        elif self.timer >= SkeletonPet.PICK_INTERVAL:
            deltaX = self.dest_x - self.x
            deltaY = self.dest_y - self.y
            base = getBase(deltaX, deltaY)
            if base != 0:
                self.velocity_x = (deltaX / base) * SkeletonPet.SPEED
                self.velocity_y = (deltaY / base) * SkeletonPet.SPEED
            else:
                self.destPicked = False
                self.timer = 0
                self.velocity_x = 0
                self.velocity_y = 0
            if abs(self.dest_x - self.x) < .05 and abs(self.dest_y - self.y) < .05 or self.timer >= SkeletonPet.MAX_PICK_DURATION:
                self.destPicked = False
                self.timer = 0
                self.velocity_x = 0
                self.velocity_y = 0

        self.rect.center = (self.x * pixel_per_block, self.y * pixel_per_block)


# inventory slots: 8 x 4
# inventory item 35x35 (ppb: 64)
# slot 1  topleft: (140, 212.5)
# slot 2  topleft: (180, 212.5) # deltaX = 40
# slot 9  topleft: (140, 212.5)
# slot 17 topleft: (140, 252.5) # deltaY = 40
# slot 25 topleft: (140, 292.5)

img.inventory_bg = img.inventory_bg.convert()


class InventoryItem(pygame.sprite.Sprite):

    isCursorHover = False

    def __init__(self, x, y, type, count):
        super().__init__()
        self.x = x
        self.y = y
        self.type = type
        self.count = count
        self.rarity = 'common'
        if self.type == Item.TYPE_PET_CAKE:
            self.image = img.pet_cake_item
            self.item_name = '     SkeletonPet Cake     '
            self.rarity = 'rare'
        elif self.type == Item.TYPE_HEALTH_POTION:
            self.image = img.health_potion_item
            self.item_name = '  Health  Potion  '
        elif self.type == Item.TYPE_MANA_POTION:
            self.image = img.mana_potion_item
            self.item_name = '   Mana  Potion   '
        elif self.type == Item.TYPE_TIER_1_WAND:
            self.image = img.tier_1_wand_item
            self.item_name = '   Tier 1  Wand   '
            self.rarity = 'legendary'
        elif self.type == Item.TYPE_TIER_2_WAND:
            self.image = img.tier_2_wand_item
            self.item_name = '   Tier 2  Wand   '
            self.rarity = 'legendary'
        elif self.type == Item.TYPE_SKELETON_PET_SPAWN_EGG:
            self.image = img.skeleton_spawn_egg_item
            self.item_name = 'Skeleton Spawn Egg'
            self.rarity = 'epic'
        elif self.type == Item.TYPE_SPEEDUP_BOOST:
            self.image = img.speedup_boost_item
            self.item_name = ' Speedup  Boost '
            self.rarity = 'epic'
        if self.rarity == 'common':
            self.item_name = toolBarFont.render(self.item_name, True, GREEN)
        elif self.rarity == 'rare':
            self.item_name = toolBarFont.render(self.item_name, True, BLUE)
        elif self.rarity == 'epic':
            self.item_name = toolBarFont.render(self.item_name, True, PURPLE)
        elif self.rarity == 'legendary':
            self.item_name = toolBarFont.render(self.item_name, True, GOLD)

        self.rect = self.image.get_rect()
        inventory_group.add(TextDisplay(
            self.x / pixel_per_block, self.y / pixel_per_block,
            str(self.count), toolBarFont, WHITE, 0, False))
        self.rect.topleft = (self.x, self.y)

    def update(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if abs(self.x + 257 - mouse_x) <= 17 and abs(self.y + 65 - mouse_y) <= 17:
            global inventoryChanged
            inventoryChanged = True
            inventory_surface.blit(self.item_name, (self.x - 35, self.y - 11))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 3:
                        if self.type == Item.TYPE_SKELETON_PET_SPAWN_EGG:
                            skeleton_pet_group.add(
                                SkeletonPet(player.x, player.y, SkeletonPet.TYPE_SKELETON))
                            player.inventory[Item.TYPE_SKELETON_PET_SPAWN_EGG].count -= 1
                        elif self.type == Item.TYPE_HEALTH_POTION:
                            useHealthPotion()
                        elif self.type == Item.TYPE_MANA_POTION:
                            useManaPotion()
                        elif self.type == Item.TYPE_SPEEDUP_BOOST:
                            Player.SPEED *= ItemDrop.SPEED_UP_BOOST_RATE
                            effect_group.add(
                                Effect(player.x, player.y, 'boost'))
                            player.inventory[Item.TYPE_SPEEDUP_BOOST].count -= 1
                        elif self.type == Item.TYPE_PET_CAKE:
                            player.inventory[Item.TYPE_PET_CAKE].count -= 1
                            item_drop_group.add(
                                ItemDrop(player.x - 1, player.y, ItemDrop.TYPE_PET_CAKE))


# Inventory


inventory_surface = pygame.Surface((int(480 * img.fix), int(480 * img.fix)))


def renderInventory():
    global inventoryChanged
    inventoryChanged = False
    inventory_group.empty()
    count = 1
    for item in player.inventory:
        if item.count > 0:
            if count <= 8:
                inventory_group.add(InventoryItem(
                    82 + (count - 1) * 40, 281, item.type, item.count))
            elif count <= 16:
                inventory_group.add(InventoryItem(
                    82 + (count - 9) * 40, 321, item.type, item.count))
            elif count <= 24:
                inventory_group.add(InventoryItem(
                    82 + (count - 17) * 40, 361, item.type, item.count))
            elif count <= 32:
                inventory_group.add(InventoryItem(
                    82 + (count - 25) * 40, 401, item.type, item.count))
            count += 1

    inventory_surface.blit(img.inventory_bg, (0, 0))
    inventory_surface.blit(img.playerImg, (327, 120))
    inventory_group.draw(inventory_surface)


# Instances
mouse = Mouse(img.aimImg)
aim.add(mouse)

playerHealthBar = PlayerHealthBar()
playerManaBar = PlayerManaBar()
bar_group.add(playerHealthBar)
bar_group.add(playerManaBar)

coin_status = StatusCoin()
status_group.add(coin_status)

base_toolBar_surface = pygame.Surface((int(344 * img.fix), int(64 * img.fix)))

base_toolBar_surface.blit(img.toolBarImg, (0, 0))
base_toolBar_surface.blit(pygame.transform.scale(
    img.health_potion_sprites[0], (int(58 * img.fix), int(58 * img.fix))), (int(6 * img.fix), int(2 * img.fix)))
base_toolBar_surface.blit(pygame.transform.scale(
    img.mana_potion_sprites[0], (int(58 * img.fix), int(58 * img.fix))), (int(75 * img.fix), int(2 * img.fix)))


Key_q = toolBarFont.render("q Ai:z", True, BLACK)
Key_e = toolBarFont.render("e Ai:x", True, BLACK)
Key_1 = toolBarFont.render("1", True, BLACK)
Key_2 = toolBarFont.render("2", True, BLACK)
Key_3 = toolBarFont.render("3", True, BLACK)

base_toolBar_surface.blit(Key_q, (int(6 * img.fix), int(2 * img.fix)))
base_toolBar_surface.blit(Key_e, (int(75 * img.fix), int(2 * img.fix)))
base_toolBar_surface.blit(Key_1, (int(143 * img.fix), int(3 * img.fix)))
base_toolBar_surface.blit(Key_2, (int(212 * img.fix), int(3 * img.fix)))
base_toolBar_surface.blit(Key_3, (int(280 * img.fix), int(3 * img.fix)))

# GameLoop

GameStart = False
levelCleared = False
gameRunning = True
GameRest = False
bossKilled = False
display_toolBar = False
updated = False
screenShake = False
screenShake_changeDirection = False
displayInventory = False
inventoryChanged = True
currMob_count = 0
level = 1
kill_needed = 0
kill_cnt = 0
kill_needed = ((level + 2) ** 2) * 2 + 1
finalScore = 0
counter = 0
gameRender_y = 0


def useHealthPotion():
    if player.health < 100:
        if player.inventory[Item.TYPE_HEALTH_POTION].count > 0:
            player.inventory[Item.TYPE_HEALTH_POTION].count -= 1
            player.health += Potion.HEALTH_POTION_REGEN
            aud.usePotionSound.play()
            global inventoryChanged
            inventoryChanged = True


def useManaPotion():
    if player.mana < Player.MAX_MANA:
        if player.inventory[Item.TYPE_MANA_POTION].count > 0:
            player.inventory[Item.TYPE_MANA_POTION].count -= 1
            player.mana += Potion.MANA_POTION_REGEN
            aud.usePotionSound.play()
            global inventoryChanged
            inventoryChanged = True


def updateGame():
    global GameStart, GameRest, mapChanged, currMap

    if mapChanged:
        block_group.empty()
        for y in range(len(currMap)):
            for x in range(len(currMap[y])):
                block_group.add(Block(currMap[y][x], x, y))
        mapChanged = False

    aim.update()
    player_group.update()
    if GameStart:
        if not GameRest:
            boss_group.update()
            slime_group.update()
            boss_health_bar_group.update()
        fireball_group.update()
        electricball_group.update()
        wand_group.update()
    staticEffect_group.update()
    bar_group.update()
    effect_group.update()
    item_drop_group.update()
    portal_group.update()
    text_display_group.update()
    static_instance_group.update()
    if displayInventory:
        if inventoryChanged:
            renderInventory()
        inventory_group.update()
    npc_group.update()
    skeleton_pet_group.update()


toolBar_slot_1 = (int(143 * img.fix), int(2 * img.fix))
toolBar_slot_2 = (int(213 * img.fix), int(2 * img.fix))

boss_level = font.render('Boss Level', True, RED)

healthPotion_slot = (int(4 * img.fix), int(50 * img.fix))
manaPotion_slot = (int(72 * img.fix), int(50 * img.fix))

selectedBar_slot_1 = (int(136 * img.fix), 0)
selectedBar_slot_2 = (int(204 * img.fix), 0)
selectedBar_slot_3 = (int(272 * img.fix), 0)


toolBar_surf_pos = (int(screen_width / 2 - 172 * img.fix),
                    int(screen_height - 80 * img.fix))


def drawGame():
    global display_toolBar, GameStart, GameRest

    player_coin = toolBarFont.render(str(player.coin), True, WHITE)
    mana_point = toolBarFont.render(str(int(player.mana)), True, WHITE)
    player_health = toolBarFont.render(str(int(player.health)), True, WHITE)
    game_level = toolBarFont.render(
        "Level " + str(level), True, WHITE)
    time_passed = toolBarFont.render(
        "Time  " + str(counter), True, WHITE)
    score_board = toolBarFont.render(
        "Score " + str(int(player.score)), True, WHITE)
    kill_board = toolBarFont.render(
        "kill: " + str(kill_cnt) + " / " + str(kill_needed), True, WHITE)

    block_group.draw(buffer_surface)
    staticEffect_group.draw(buffer_surface)
    item_drop_group.draw(buffer_surface)
    if not GameRest:
        slime_group.draw(buffer_surface)
        boss_group.draw(buffer_surface)
        boss_health_bar_group.draw(buffer_surface)
    portal_group.draw(buffer_surface)
    static_instance_group.draw(buffer_surface)
    npc_group.draw(buffer_surface)
    player_group.draw(buffer_surface)
    skeleton_pet_group.draw(buffer_surface)
    fireball_group.draw(buffer_surface)
    electricball_group.draw(buffer_surface)
    wand_group.draw(buffer_surface)
    if display_toolBar:
        status_group.draw(buffer_surface)
        buffer_surface.blit(
            player_coin, (coin_status.x + 10, coin_status.y - 7))
        bar_group.draw(buffer_surface)
        buffer_surface.blit(mana_point, (510, 475))
        buffer_surface.blit(player_health, (322, 475))
    effect_group.draw(buffer_surface)
    if GameStart:
        buffer_surface.blit(game_level, (200, 10))
        buffer_surface.blit(time_passed, (300, 10))
        buffer_surface.blit(score_board, (400, 10))
        if level % BOSS_INTERVAL != 0:
            buffer_surface.blit(kill_board, (540, 10))
        else:
            buffer_surface.blit(boss_level, (540, 10))

    # toolBar display (base_toolBar contains the bg, health potion, and mana potion)
    toolBar_surface.blit(base_toolBar_surface, (0, 0))
    if player.wand_level[0] > 0:
        toolBar_surface.blit(img.toolBar_tier_1_wand, toolBar_slot_1)
    if player.wand_level[1] > 0:
        toolBar_surface.blit(img.toolBar_tier_2_wand, toolBar_slot_2)

    health_potion_amt = toolBarFont.render(
        str(player.inventory[Item.TYPE_HEALTH_POTION].count), False, WHITE)
    mana_potion_amt = toolBarFont.render(
        str(player.inventory[Item.TYPE_MANA_POTION].count), False, WHITE)

    if player.wand_tier == 1:
        toolBar_surface.blit(img.selectedBarImg, selectedBar_slot_1)
    elif player.wand_tier == 2:
        toolBar_surface.blit(img.selectedBarImg, selectedBar_slot_2)
    elif player.wand_tier == 3:
        toolBar_surface.blit(img.selectedBarImg, selectedBar_slot_3)

    toolBar_surface.blit(health_potion_amt, healthPotion_slot)
    toolBar_surface.blit(mana_potion_amt, manaPotion_slot)

    if display_toolBar:
        buffer_surface.blit(toolBar_surface, toolBar_surf_pos)

    #
    text_display_group.draw(buffer_surface)
    if displayInventory:
        buffer_surface.blit(inventory_surface, (240, 48))
        inventory_text.draw(buffer_surface)
    aim.draw(buffer_surface)


# Game Parameter
MOB_COUNT = 0

MAX_FRAME_RATE = 120
BOSS_INTERVAL = 5
ADD_SLIMES_PER_LEVEL = 2.8
SCREEN_SHAKE_EXTENT = 10  # px
############## Without these lines below, game cannot start !!! ##############
portal_group.add(
    Portal(14, 4.5, 1, 4, Portal.TYPE_PURPLE_PORTAL, Portal.USAGE_START_GAME))
##############################################################################
# player.mana = 9999
# player.coin = 1000000
# skeleton_pet_group.add(SkeletonPet(4, 6, SkeletonPet.TYPE_SKELETON))

while gameRunning:

    # Level Settings
    Boss.STARTING_HEALTH = (level / 3) * 1200

    if level % BOSS_INTERVAL != 0:
        if kill_cnt >= kill_needed:
            kill_needed = ((level + 2) ** 2) * 2 + 1
            levelCleared = True
            kill_cnt = 0
    else:
        if bossKilled:
            levelCleared = True
            bossKilled = False
            kill_cnt = 0

    # detect if the level is cleared
    if levelCleared and not updated:
        text_display_group.add(TextDisplay(
            3.1, 3, 'Level Clear', clearLevelFont, WHITE, 100, True, True, False))
        GameRest = True
        slime_group.empty()
        portal_group.add(
            Portal(14, 4.5, 1, 4, Portal.TYPE_PURPLE_PORTAL, Portal.USAGE_SAFE_HOUSE))
        Boss.SCORE_PER_KILL *= 1.08
        updated = True

    MOB_COUNT = int(level * ADD_SLIMES_PER_LEVEL)

    if currMob_count < MOB_COUNT and not GameRest and GameStart:
        Slime.STARTING_HEALTH = 15 * (1 + (level / 10) * 3)
        Slime.SPEED = .012 * (1 + (level / 10) * 2) * velocity_fix
        Slime.MAX_COIN_DROP = int(2 * (1 + (level / 10) * 4))
        for iter in range(MOB_COUNT - currMob_count):
            Slime.generateSlime()
        currMob_count = MOB_COUNT
        if level % BOSS_INTERVAL == 0:
            Boss.STARTING_HEALTH = 2400 * (2 ** (level / BOSS_INTERVAL - 1))
            spawnBoss()
    # Detecting Events
    if player.health <= 0:
        gameRunning = False
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            gameRunning = False
            pygame.quit()
            sys.exit()
            break

        if event.type == pygame.USEREVENT:
            if GameStart and not GameRest:
                counter += 1
                # player.score += 1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player.velocity_y = -Player.SPEED
            if event.key == pygame.K_s:
                player.velocity_y = Player.SPEED
            if event.key == pygame.K_a:
                player.velocity_x = -Player.SPEED
            if event.key == pygame.K_d:
                player.velocity_x = Player.SPEED
            if event.key == pygame.K_q:
                player.usingHealthPotion = True
            if event.key == pygame.K_e:
                player.usingManaPotion = True
            if event.key == pygame.K_z:
                player.autoHealthPotion = not player.autoHealthPotion
            if event.key == pygame.K_x:
                player.autoManaPotion = not player.autoManaPotion
            if event.key == pygame.K_r:
                display_toolBar = not display_toolBar
            if event.key == pygame.K_b:
                displayInventory = not displayInventory
            if event.key == pygame.K_1:
                if Wand.isWandUnlocked(1):
                    player.wand_tier = 1
                    aud.clickButtonSound.play()
            if event.key == pygame.K_2:
                if Wand.isWandUnlocked(2):
                    player.wand_tier = 2
                    aud.clickButtonSound.play()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player.velocity_y = 0
            if event.key == pygame.K_s:
                player.velocity_y = 0
            if event.key == pygame.K_a:
                player.velocity_x = 0
            if event.key == pygame.K_d:
                player.velocity_x = 0
            if event.key == pygame.K_q:
                player.usingHealthPotion = False
            if event.key == pygame.K_e:
                player.usingManaPotion = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if (event.button == 1) and not GameRest:
                if player.wand_tier == 1:
                    if player.mana > 0:
                        player.mana -= 1
                        aud.shootFireball.play()
                        Fireball.generate()
                elif player.wand_tier == 2:
                    if player.mana >= 2:
                        player.mana -= 2
                        aud.shootElectricball.play()
                        Electricball.generate()
            if event.button == 2 and not GameRest:
                player.shooting = True
            if event.button == 4 and GameStart:
                if player.wand_tier + 1 > Wand.MAX_TIER:
                    player.wand_tier = 1
                elif Wand.isWandUnlocked(player.wand_tier + 1):
                    player.wand_tier += 1
            if event.button == 5 and GameStart:
                player.wand_tier -= 1
                if player.wand_tier < 1:
                    temp_tier = Wand.MAX_TIER
                    while not Wand.isWandUnlocked(temp_tier):
                        temp_tier -= 1
                    player.wand_tier = temp_tier
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 2:
                player.shooting = False

    # Contents
    if player.shooting and not GameRest:
        if player.wand_tier == 1:
            if player.mana >= Wand.TIER1_MANA_COST:
                player.mana -= Wand.TIER1_MANA_COST
                Fireball.generate()
                aud.shootFireball.play()
        elif player.wand_tier == 2:
            if player.mana >= Wand.TIER2_MANA_COST:
                player.mana -= Wand.TIER2_MANA_COST
                Electricball.generate()
                aud.shootElectricball.play()

    if player.usingHealthPotion:
        useHealthPotion()
    if player.usingManaPotion:
        useManaPotion()
    if player.autoHealthPotion:
        if player.health < Player.AUTO_HEALTH_POTION_LINE:
            useHealthPotion()
    if player.autoManaPotion:
        if player.mana < Player.AUTO_MANA_POTION_LINE:
            useManaPotion()

    # Regular Update
    updateGame()
    # draw Game to buffer_surface
    drawGame()
    # render buffer_surface
    if screenShake:
        if not screenShake_changeDirection:
            gameRender_y += 1
        else:
            gameRender_y -= 1

        if gameRender_y >= SCREEN_SHAKE_EXTENT:
            screenShake_changeDirection = True
        elif gameRender_y <= -SCREEN_SHAKE_EXTENT:
            screenShake_changeDirection = False

        screen.blit(buffer_surface, (0, gameRender_y))

    else:
        screen.blit(buffer_surface, (0, 0))
    pygame.display.update()

    clock.tick(MAX_FRAME_RATE)


endGame = True

screen.blit(img.menuBackground, (-480, -312))


myFile = open("saves/highestScore.txt", 'r+')

higestScore = int(myFile.read())

if player.score > higestScore:
    myFile.write(str(player.score))
    higestScore = player.score

myFile.close()

score_board = font.render(
    "Final Score " + str(int(player.score)), True, RED)
currSprite = 0

while endGame:
    screen.blit(img.endGame_sprites[int(currSprite)], (80, 100))
    currSprite += .1
    if currSprite >= len(img.endGame_sprites):
        currSprite = 0
    rand_color = (random.randrange(0, 255), random.randrange(
        0, 255), random.randrange(0, 255))
    highest_score = font.render(
        "Highest Score " + str(int(player.score)), True, rand_color)
    screen.blit(score_board, (400, 300))
    screen.blit(highest_score, (400, 350))

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                endGame = False
                aud.clickButtonSound.play()
                sys.exit()
        if event.type == pygame.QUIT:
            endGame = False
            pygame.quit()
            sys.exit()
