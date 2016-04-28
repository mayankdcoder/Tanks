from main import Game
from constants import Constants


__author__ = 'capt_MAKO'
__since__ = '30/December/2015 21:45:00'
__version__ = '1.0'


constants = Constants()
main = Game(constants)
main.intro()
main.main_loop()
