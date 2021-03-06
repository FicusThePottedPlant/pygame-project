import os
import sys

import pygame


def load_image(name, colorkey=None):
    """load image macros"""
    fullname = os.path.join('data/sprites', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image
