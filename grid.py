import pygame

from block import *

GRID_ROWS = 20
GRID_COLUMNS = 10

GRID_SIZE = 24
GRID_X_OFFSET = (GRID_SIZE*9 - 7)

FALL_TIME = 1000

class Grid(object):
	def __init__(self):
		self.blocks = []
		for row in range(GRID_ROWS):
		    row_list = []
		    for column in range(GRID_COLUMNS):
		        row_list.append(None)
		    self.blocks.append(row_list) 
		    
		self.blocks[0][0] = Block()
		self.falling_time = pygame.time.get_ticks() + FALL_TIME
		
		self.bg = pygame.image.load('images/bg.png').convert()
		
	def draw(self):
	    surf = pygame.display.get_surface()
	    
	    surf.blit(self.bg, (0,0))
	    
	    for row in range(GRID_ROWS):
	        for column in range(GRID_COLUMNS):
	            if self.blocks[row][column]:
	                self.blocks[row][column].draw(
	                    column*GRID_SIZE + GRID_X_OFFSET, row*GRID_SIZE, surf)
		
	def update(self, game):
	    if pygame.time.get_ticks() >= self.falling_time:
	        for row in range(GRID_ROWS-1,-1,-1):
	            for column in range(GRID_COLUMNS-1,-1,-1):
	                if (self.blocks[row][column]):
	                    self.blocks[row+1][column] = self.blocks[row][column]
	                    self.blocks[row][column] = None
	                
	        self.falling_time = pygame.time.get_ticks() + FALL_TIME