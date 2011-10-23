import pygame
import pygame.locals as local

from grid import *
from menu import *
from block import *

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

STATE_MENU = 0
STATE_GAME = 1

class Game(object):
    def __init__(self):
        pygame.init()

        # Create our display.
        self.display = pygame.display.set_mode(
            (SCREEN_WIDTH, SCREEN_HEIGHT))
            
        # Game is running! Or not.
        self.is_running = False
        
        # Current game state.
        self.state = STATE_MENU
	self.firstTime = 1
        
        # key presses for the current frame
        self.key_presses = {}
        
        # Timer business.
        self.fps_timer = pygame.time.Clock()
		
    def run(self):
	    # The game should be running now!
        self.is_running = True
		
		# Create our main game objects.
        self.menu = Menu()
        self.grid = Grid()
		
		# Loop while the game is running, obviously
        while self.is_running:
			# Read in SDL events.
            for event in pygame.event.get():
                if event.type == local.QUIT:
					# Window close event.
                    self.is_running = False
                elif event.type == local.KEYDOWN:
                    self.key_presses[event.key] = True
			
			# Update and draw the right thing depedning on the
			# game state!
            if self.state == STATE_MENU:
			    self.menu.update(self)
			    self.menu.draw()
            elif self.state == STATE_GAME:
                self.grid.update(self)
                self.grid.draw()

            if local.K_m in self.key_presses:
	                    self.state = STATE_MENU
            # Flip the display.
            pygame.display.update()
            
            # Reset the key presses
            self.key_presses = {}
            
            # Wait for the next frame, yoslice.
            self.fps_timer.tick(60)
            
            
