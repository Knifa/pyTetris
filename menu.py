import pygame
import pygame.locals as local


class Menu(object):
    def __init__(self):
    	pass

    def update(self,game):
	if local.K_COMMA in game.key_presses:
		print "Yes!"

    def draw(self):
	surf = pygame.display.get_surface()
