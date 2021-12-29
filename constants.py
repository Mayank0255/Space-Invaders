import pygame
import os
import sys


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# from screens.background import slow_bg_obj


# ROOT VARS
TITLE = 'SPACE INVADERS'
WIDTH = 750
HEIGHT = 750

# Canvas Dimensions
CANVAS = pygame.display.set_mode((WIDTH, HEIGHT))

screen_rect = CANVAS.get_rect()
center_x = screen_rect.centerx
center_y = screen_rect.centery

# Load Background Image
backgroundImage = pygame.image.load(os.path.join(
    'assets', 'graphics', 'background-black.png'))

# Set Background Dimensions
BG = pygame.transform.scale(backgroundImage, (WIDTH, HEIGHT))

FPS = 60
framespersec = pygame.time.Clock()

score_list = []

# list of all game sounds
soundList = []

# Initialize Sound System
pygame.mixer.init()

# PATH VARS
FONT_PATH = os.path.join('assets', 'fonts')
EXPLOSION_PATH = os.path.join('assets', 'graphics', 'explosion')

# Load Controls Image
controlImage = pygame.image.load(resource_path(
    os.path.join('assets', 'graphics', 'joystick.png')))
trophyImage = pygame.image.load(resource_path(
    os.path.join('assets', 'graphics', 'trophy.png')))

goBackImage = pygame.image.load(
    os.path.join('assets', 'graphics', 'back2.png'))
# goBackImage = pygame.transform.scale()
goBackImage = pygame.transform.scale(goBackImage, (34*2.4, 19*2.4))

# Load Hearts
heartImage = pygame.image.load(resource_path(
    os.path.join('assets', 'graphics', 'heart.png')))

# Load Enemy Ships
EASY_SPACE_SHIP = pygame.image.load(resource_path(
    os.path.join('assets', 'graphics', 'easy.png')))
MEDIUM_SPACE_SHIP = pygame.image.load(resource_path(
    os.path.join('assets', 'graphics', 'medium.png')))
HARD_SPACE_SHIP = pygame.image.load(resource_path(
    os.path.join('assets', 'graphics', 'hard.png')))
BOSS_SHIP = pygame.image.load(resource_path(
    os.path.join('assets', 'graphics', 'boss.png')))

# Load Player
PLAYER_SPACE_SHIP = pygame.image.load(resource_path(
    os.path.join('assets', 'graphics', 'retro-spaceship.png')))
PLAYER_LASER = pygame.image.load(resource_path(
    os.path.join('assets', 'graphics', 'pixel_laser_cosmic.png')))

# Load Lasers
RED_LASER = pygame.image.load(resource_path(
    os.path.join('assets', 'graphics', 'pixel_laser_red.png')))
BLUE_LASER = pygame.image.load(resource_path(
    os.path.join('assets', 'graphics', 'pixel_laser_blue.png')))
GREEN_LASER = pygame.image.load(resource_path(
    os.path.join('assets', 'graphics', 'pixel_laser_green.png')))
FLAME_LASER = pygame.image.load(resource_path(
    os.path.join('assets', 'graphics', 'pixel_laser_flame.png')))

# load music
GAME_MUSIC_PATH = resource_path(os.path.join('assets', 'sounds', 'ingame.wav'))
MENU_MUSIC_PATH = resource_path(os.path.join('assets', 'sounds', 'menu.wav'))

# sfx
PLAYER_LASER_SOUND = pygame.mixer.Sound(resource_path(
    os.path.join('assets', 'sounds', 'ownlaser.wav')))
ENEMY_LASER_SOUND = pygame.mixer.Sound(resource_path(
    os.path.join('assets', 'sounds', 'enemylaser.wav')))
EXPLODE_SOUND = pygame.mixer.Sound(resource_path(
    os.path.join('assets', 'sounds', 'explode.wav')))
LASER_HIT_SOUND = pygame.mixer.Sound(resource_path(
    os.path.join('assets', 'sounds', 'laser_hit.wav')))

# adding sounds to the list
soundList.append(PLAYER_LASER_SOUND)
soundList.append(ENEMY_LASER_SOUND)
soundList.append(EXPLODE_SOUND)
soundList.append(LASER_HIT_SOUND)
