import pygame
import os

TITLE = "Mega Man Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
FONT_STYLE = "freesansbold.ttf"
MOTO_TYPE = "motoca"
DEFAULT_TYPE = "default"
GAME_SPEED = 20

IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

ICON = pygame.image.load(os.path.join(IMG_DIR, "megaman_icon.png"))
MENU = pygame.image.load(os.path.join(IMG_DIR, "Other/menu.png"))
GAME_OVER = pygame.image.load(os.path.join(IMG_DIR, "Other/mega_gameOver.png"))

MEGA_RUN = [
    pygame.image.load(os.path.join(IMG_DIR, "mega_run/megaRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "mega_run/megaRun2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "mega_run/megaRun3.png")),
]

MEGA_RUN_BALA = [
    pygame.image.load(os.path.join(IMG_DIR, "mega_run/mega_runBala1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "mega_run/mega_runBala2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "mega_run/mega_runBala3.png")),
]

MOTO_RUN = [
    pygame.image.load(os.path.join(IMG_DIR, "mega_run/mega_moto1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "mega_run/mega_moto2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "mega_run/mega_moto3.png")),
]

MOTO_JUMP = pygame.image.load(os.path.join(IMG_DIR, "mega_run/mega_motojump.png"))

MEGA_JUMP = pygame.image.load(os.path.join(IMG_DIR, "mega_jump/megaJump.png"))

MEGA_JUMP_BALA = pygame.image.load(os.path.join(IMG_DIR, "mega_jump/mega_jumpBala.png"))

MEGA_DUCK = pygame.image.load(os.path.join(IMG_DIR, "mega_duck/megaDuck.png"))

MOTO_DUCK = pygame.image.load(os.path.join(IMG_DIR, "mega_run/mega_moto3.png"))

SMALL_ROBOT = [
    pygame.image.load(os.path.join(IMG_DIR, "mega_enemy/mega_robo1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "mega_enemy/mega_robo2.png")),
]

LARGE_ROBOT_GREEN =[
    pygame.image.load(os.path.join(IMG_DIR, "mega_enemy/mega_largRoboG1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "mega_enemy/mega_largRoboG2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "mega_enemy/mega_largRoboG3.png")),
]

LARGE_ROBOT_RED =[
    pygame.image.load(os.path.join(IMG_DIR, "mega_enemy/mega_largRoboR1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "mega_enemy/mega_largRoboR2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "mega_enemy/mega_largRoboR3.png")),
]

MEGA_VESPA =[
    pygame.image.load(os.path.join(IMG_DIR, "mega_enemy/mega_vespa1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "mega_enemy/mega_vespa2.png")),
]

MEGA_BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "mega_enemy/mega_bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "mega_enemy/mega_bird2.png")),
]

MEGA_ROBOT_FLYR = [
    pygame.image.load(os.path.join(IMG_DIR, "mega_enemy/mega_roboFlyR1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "mega_enemy/mega_roboFlyR2.png")),
]

MEGA_ROBOT_FLYG = [
    pygame.image.load(os.path.join(IMG_DIR, "mega_enemy/mega_roboFlyG1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "mega_enemy/mega_roboFlyG2.png")),
]

MEGA_ROBOT_FLY = [
    pygame.image.load(os.path.join(IMG_DIR, "mega_enemy/mega_roboFly1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "mega_enemy/mega_roboFly2.png")),
]

CLOUD = [pygame.image.load(os.path.join(IMG_DIR, 'Other/mega_cloud.png'))]

MEGA_MOTO = pygame.image.load(os.path.join(IMG_DIR, 'Other/mega_moto.png'))

MEGA_BALA = pygame.image.load(os.path.join(IMG_DIR, 'Other/mega_bala.png'))

LIFE = pygame.image.load(os.path.join(IMG_DIR, 'Other/life.png'))

MEGA_POWER = [
    pygame.image.load(os.path.join(IMG_DIR, 'Other/mega_power1.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Other/mega_power2.png')),
]

MBG = pygame.image.load(os.path.join(IMG_DIR, 'Other/back.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

SOUND = [
    os.path.join(IMG_DIR,"music/megalovania.mp3"),
    os.path.join(IMG_DIR,"music/BoxCat.mp3"),
]

JUMP_SOUND = os.path.join(IMG_DIR,"sounds/mario_jump.mp3")

DEATH_SOUND = os.path.join(IMG_DIR, "sounds/pacman_death.mp3")

