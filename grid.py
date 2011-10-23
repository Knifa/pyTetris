import pygame
import random

from block import *

GRID_ROWS = 20
GRID_COLUMNS = 10

GRID_SIZE = 24
GRID_X_OFFSET = (GRID_SIZE*9 - 7)

FALL_TIME = 200

class Grid(object):
    def __init__(self):
        self.blocks = []
        for row in range(GRID_ROWS):
            row_list = []
            for column in range(GRID_COLUMNS):
                row_list.append(None)
            self.blocks.append(row_list) 
        
        self.falling_time = pygame.time.get_ticks() + FALL_TIME
        self.falling_blocks = []
        
        color = random.randint(0, len(blockList)-1)
        for i in range(4):
            self.falling_blocks.append(Block(color))
        
        self.blocks[1][0] = self.falling_blocks[0]
        self.blocks[1][1] = self.falling_blocks[1]
        self.blocks[1][2] = self.falling_blocks[2]
        self.blocks[0][1] = self.falling_blocks[3]
        
        self.bg = pygame.image.load('images/bg.png').convert()
        
    def draw(self):
        surf = pygame.display.get_surface()
        
        surf.blit(self.bg, (0,0))
        
        for row in range(GRID_ROWS):
            for column in range(GRID_COLUMNS):
                if self.blocks[row][column]:
                    self.blocks[row][column].draw(
                        column*GRID_SIZE + GRID_X_OFFSET, row*GRID_SIZE)

    def check_falling_collision(self):
        # loop through the grid backwards
        for row in range(GRID_ROWS-1,-1,-1):
            for column in range(GRID_COLUMNS-1,-1,-1):                
                # is there a block there that should be falling?
                if self.blocks[row][column] in self.falling_blocks:
                    if row+1 >= GRID_ROWS:
                        return True # at bottom of screen
                    
                    if self.blocks[row+1][column] and not self.blocks[row+1][column] in self.falling_blocks:
                        print self.blocks[row+1][column]
                        return True # something below.
        
        return False
        
    def update(self, game):
        # check if it's time to move stuff down
        if pygame.time.get_ticks() >= self.falling_time:
            falling_done = False
            
            # loop through the grid backwards
            if not self.check_falling_collision():
                for row in range(GRID_ROWS-1,-1,-1):
                    for column in range(GRID_COLUMNS-1,-1,-1):
                        # is there a block there that should be falling?
                        if self.blocks[row][column] in self.falling_blocks:                         
                            # make sure it doesn't wrap round, yo
                            new_row = row + 1
                            if new_row >= GRID_ROWS:
                                falling_done = True
                            else:
                                self.blocks[new_row][column] = self.blocks[row][column]
                                self.blocks[row][column] = None
            else:
                falling_done = True
                
            if falling_done:
                for b in self.falling_blocks:
                    b.state = False
                    
                self.falling_blocks = []
                
                color = random.randint(0, len(blockList)-1)
                for i in range(4):
                    self.falling_blocks.append(Block(color))

                self.blocks[1][0] = self.falling_blocks[0]
                self.blocks[1][1] = self.falling_blocks[1]
                self.blocks[1][2] = self.falling_blocks[2]
                self.blocks[0][1] = self.falling_blocks[3]
                
            self.falling_time = pygame.time.get_ticks() + FALL_TIME
