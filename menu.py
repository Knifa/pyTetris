import pygame
import pygame.locals as local


class Menu(object):
    def __init__(self):
    	pass

    def update(self,game):
	if local.K_UP in game.key_presses:
		print "Up"
	elif local.K_DOWN in game.key_presses:
		print "Down"
	elif local.K_x in game.key_presses:
		game.state = 1

    def draw(self):
	surf = pygame.display.get_surface()
	
