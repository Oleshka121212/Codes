import pygame

pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
backgroung_image = pygame.image.load('cosmos.jpg')

while True:
	screen.blit(backgroung_image, (0, 0))
	pygame.display.update()
	clock.tick(60)
	
