import pygame as pg
import sys
from settings import *
from game_map import *
from player import *
from raycasting import *
from object_renderer import *

class Game:
   # in constructor we initialize the pygame modules
   def __init__(self):
      pg.init()
      pg.mouse.set_visible(False)
      self.screen = pg.display.set_mode(RES)  # creating screen for rendering the set resolution
      self.clock = pg.time.Clock()            # instance of the clock class for frame rate
      self.delta_time = 1                     # Delta time: is the amount of time that has passed since the last frame
      self.new_game()                         # call to the method from main app constructor
      
      # If we want the player's movement speed to be independent of the frame rate, we need to get the Delta time value for each frame
      
   def new_game(self):
      self.map = Map(self)                             # instance of the map class
      self.player = Player(self)                       # instance of the player class
      self.object_renderer = ObjectRenderer(self)      # instance of the object renderer class
      self.raycasting = RayCasting(self)               # instance of the raycasting class
   
   def update(self):
      self.player.update()
      self.raycasting.update()
      pg.display.flip()                                # update the screen
      self.delta_time = self.clock.tick(FPS)
      pg.display.set_caption(f'{self.clock.get_fps() :.1f}')
      
   def draw(self):
      # self.screen.fill('black')
      self.object_renderer.draw()
      # self.map.draw()
      # self.player.draw()

   def check_events(self):
      for event in pg.event.get():
         if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
            pg.quit()
            sys.exit()
      
   def run(self):
      # main loop
      while True:
         self.check_events()              
         self.update()
         self.draw()
         
# instance of our game with call
if __name__ == '__main__':
   game = Game()
   game.run()