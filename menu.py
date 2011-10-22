import pygame

class Menu(object):
    def __init__(self):
    	pass

    def update(self,game):
	print game.key_presses
	if "K_COMMA" in game.key_presses:
		print "Yes!"

    def draw(self):
	pass
