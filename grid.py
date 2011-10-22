import pygame

from block import *

GRID_ROWS = 20
GRID_COLUMNS = 10

GRID_SIZE = 50

class Grid(object):
	def __init__(self):
		self.blocks = []
		for column in range(GRID_COLUMNS):
		    row_list = []
		    for row in range(GRID_ROWS):
		        row_list.append(Block())
		        
		    self.blocks.append(row_list) 
		
	def draw(self):
	    surf = pygame.display.get_surface()
	    
	    for column in range(GRID_COLUMNS):
	        for row in range(GRID_ROWS):
	            self.blocks[column][row].draw(
	                column*GRID_SIZE, row*GRID_SIZE, surf)
		
	def update(self, game):
		pass
