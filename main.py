import pygame
import pygame.locals as local

from grid import *

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class Game(object):
    def __init__(self):
        pygame.init()

        # Create our display.
        self.display = pygame.display.set_mode(
            (SCREEN_WIDTH, SCREEN_HEIGHT))
            
        # Game is running! Or not.
        self.is_running = False
		
    def run(self):
	    # The game should be running now!
        self.is_running = True
		
		# Create a new game grid.
        self.grid = Grid()
		
		# Loop while the game is running, obviously
        while self.is_running:
			# Read in SDL events.
            for event in pygame.event.get():
                if event.type == local.QUIT:
					# Window close event.
                    self.is_running = False
			
			# Update and draw the grid.
            self.grid.update(self)
            self.grid.draw()
					
            # Flip the display.
            pygame.display.update()
	
game = Game()
game.run()