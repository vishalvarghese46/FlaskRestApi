import math
import os
from random import randint
from collections import deque

import pygame
from pygame.locals import *

#base variable
FPS = 60                #Frame size of the program
ANIMATION_SPEED = 0.18  #The animation speed of the program

WIN_WIDTH = 284 * 2
WIN_HEIGHT = 512

def load_images():


def main():
    pygame.init()
    display_sufrace = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption('Flappy Bird')

    clock = pygame.time.Clock()
    score_font = pygame.font.SysFont(None,32,bold=True)
    images = load_images()






