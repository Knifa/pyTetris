import pygame

class Block(object):
        def __init__(self):
            #state is a boolean, where true = falling, false = stationary
            self.state = True
            #loads the image block.png from the root dir and converts it
            #for use with the current screen.
            self.image = pygame.image.load('images/block.png').convert()
		
        #taking parameters of self, x co-ord, y co-ord, and display screen.
        def draw(self, x, y, screen):
                #draws the block at location (x,y) on display screen.
                screen.blit(self.image, (x,y))
                
        def update(self):
                #use for animation later possibly?
                pass


