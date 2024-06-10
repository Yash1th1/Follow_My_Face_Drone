import pygame
from pygame.locals import *


def init():
    pygame.init()
    window = pygame.display.set_mode((400, 400))


def getkey(keyname):
    ans = False
    for event in pygame.event.get(): pass
    keyInput = pygame.key.get_pressed()
    mykeys = getattr(pygame, 'K_{}'.format(keyname))
    if keyInput[mykeys]:
        ans = True
    pygame.display.update()
    return ans


def main():
    if getkey('LEFT'):
        print("Left Key Pressed")
    if getkey('RIGHT'):
        print("Right Key Pressed")


if __name__ == "__main__":
    init()
    while True:
        main()
