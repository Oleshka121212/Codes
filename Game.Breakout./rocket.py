import pygame
from game_objects import GameObject
import config as c

class Padle(GameObject):
	def __init__(self, x, y, w, h, color, offset):
		GameObject.__init__(self, x, y, w, h)
		self.color = color
		self.offset = offset
		self.moving_left = False
		self.moving_right = False

	def draw(self):
		pygame.draw.rect(surface, self.color, self.bounds)
