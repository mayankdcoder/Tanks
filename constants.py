__author__ = 'capt_MAKO'
__since__ = '30/December/2015 21:45:00'
__version__ = '1.0'

from pygame import init, font


class Constants:
    white = (255, 255, 255)
    black = (0, 0, 0)
    green = (0, 255, 0)
    red = (255, 0, 0)
    yellow = (255, 255, 0)
    light_green = (0, 255, 0)
    light_red = ()
    light_yellow = ()
    small_fonts = object()
    medium_fonts = object()
    large_fonts = object()

    def __init__(self):
        init()
        self.small_fonts = font.SysFont("comicsansms", 25)
        self.medium_fonts = font.SysFont('comicsansms', 50)
        self.large_fonts = font.SysFont('comicsansms', 75)
