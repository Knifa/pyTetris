import pygame
import pygame.locals as local


class Menu(object):
    def __init__(self):
    	self.Resume = 1
	self.Options = 0
	self.Quit = 0

    def update(self,game):
	if local.K_UP in game.key_presses:
		if self.Options == 1:
			self.Resume = 1
			self.Options = 0
		elif self.Quit == 1:
			self.Options = 1
			self.Quit = 0
	elif local.K_DOWN in game.key_presses:
		if self.Resume == 1:
			self.Options = 1
			self.Resume = 0
		elif self.Options == 1:
			self.Quit = 1
			self.Options = 0
	elif local.K_x in game.key_presses:
		if self.Resume == 1:
			game.state = 1
		elif self.Quit == 1:
			quit()

    def draw(self):
	surf = pygame.display.get_surface()
	
