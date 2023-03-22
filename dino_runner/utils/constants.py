import pygame
import os
# Global Constants
TITLE = "Dino Dino"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
FONT_STYLE = "freesansbold.ttf"

IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

MEGA_RUN = [
    pygame.image.load(os.path.join(IMG_DIR, "mega/megaRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "mega/megaRun2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "mega/megaRun3.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJump.png"))

MEGA_JUMP = pygame.image.load(os.path.join(IMG_DIR, "mega/megaJump.png"))

JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpShield.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

MEGA_DUCK = pygame.image.load(os.path.join(IMG_DIR, "mega/megaDuck.png"))

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]

SMALL_ROBOT = [
    pygame.image.load(os.path.join(IMG_DIR, "mega/mega_robo1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "mega/mega_robo2.png")),
    ]

LARGE_ROBOT =[
    pygame.image.load(os.path.join(IMG_DIR, "mega/mega_largRobo1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "mega/mega_largRobo2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "mega/mega_largRobo3.png")),
    ]

LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]
LARGE_CANO = [
    pygame.image.load(os.path.join(IMG_DIR, "mega/LargeCano1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "mega/LargeCano2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "mega/LargeCano3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]

BIRD_RED = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird_red1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird_red2.png")),
]

BIRD_GREEN = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird_green1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird_green2.png")),
]

BIRD_BLUE = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird_blue1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird_blue2.png")),
]

MEGA_VESPA =[
    pygame.image.load(os.path.join(IMG_DIR, "mega/mega_vespa1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "mega/mega_vespa2.png")),
]

MEGA_BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "mega/mega_bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "mega/mega_bird2.png")),
]

CLOUD = [pygame.image.load(os.path.join(IMG_DIR, 'mega/mega_cloud2.png'))]
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

MBG = pygame.image.load(os.path.join(IMG_DIR, 'mega/back.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))


SOUND = [
    os.path.join(IMG_DIR,"music/megalovania.mp3"),
    os.path.join(IMG_DIR,"music/BoxCat.mp3"),
]

JUMP_SOUND = os.path.join(IMG_DIR,"sounds/mario_jump.mp3")

DEATH_SOUND = os.path.join(IMG_DIR, "sounds/pacman_death.mp3")


DEFAULT_TYPE = "default"
