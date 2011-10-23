import pygame
import pygame.locals as local

class Menu(object):
    def __init__(self):
    	self.Resume = 1
	self.Options = 0
	self.Quit = 0
	self.bg = pygame.image.load('images/menubg.png')
	self.ResumePressed = pygame.image.load('images/button1.png')
	self.ResumeUnpressed = pygame.image.load('images/button2.png')
	self.OptionsPressed = pygame.image.load('images/button1.png')
	self.OptionsUnpressed = pygame.image.load('images/button2.png')
	self.QuitPressed = pygame.image.load('images/button1.png')
	self.QuitUnpressed = pygame.image.load('images/button2.png')
	self.screen = pygame.display.get_surface()
    def update(self,game):
	if self.Resume == 1:
		self.bg.blit(self.ResumePressed, (240,240))
		self.bg.blit(self.OptionsUnpressed, (240,304))
		self.bg.blit(self.QuitUnpressed, (240,368))
	elif self.Options == 1:
		self.bg.blit(self.ResumeUnpressed, (240,240))
		self.bg.blit(self.OptionsPressed, (240,304))
		self.bg.blit(self.QuitUnpressed, (240,368))
	else:
		self.bg.blit(self.ResumeUnpressed, (240,240))
		self.bg.blit(self.OptionsUnpressed, (240,304))
		self.bg.blit(self.QuitPressed, (240, 368))
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
	self.screen.blit(self.bg, (1,1))
	
