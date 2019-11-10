import pygame
import random


pygame.init()


pygame.display.set_caption("Game")
ScreenWidth, ScreenHeight = 1100, 600 
player_image = pygame.image.load("Background.jpg.png")
player_vs_image = pygame.image.load("Player_vs.png")
back_ground = pygame.image.load("Background_image.png")

win = pygame.display.set_mode((ScreenWidth, ScreenHeight))
clock = pygame.time.Clock()

class Player_vs():
	def __init__(self, x, y, width, height, vel):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.vel = vel
		self.hitbox = (ScreenWidth-130, self.y, 140, 130)

	def draw(self):
		win.blit(player_vs_image, (self.x, self.y))
		self.hitbox = (ScreenWidth-150, self.y, 140, 130)
		#pygame.draw.rect(win, (250, 0, 0), self.hitbox, 2)

	def hit(self):
		print("hit")

class Player():
	def __init__(self, x, y, width, height, vel):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.vel = vel
		self.hitbox = (self.x, self.y, 140, 130)
		
	def draw(self):
		win.blit(player_image, (self.x, self.y))
		self.hitbox = (self.x, self.y, 140, 130)
		#pygame.draw.rect(win,(250, 0, 0), self.hitbox, 2)

	def hit(self):
		print('hit')

class Bullet():
	def __init__(self, x, y, color = (255, 0, 0), radius = 5, vel = 15):
		self.x = x
		self.y = y
		self.color = color
		self.radius = radius
		self.vel = vel
		self.facing = vel * 8

	def draw(self):
		pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
	
def redrawWindow():
	pygame.display.update()
	win.blit(back_ground, (0, 0))
	sq.draw()
	bot.draw()
	for bullet in bullets_bot:
		bullet.draw()
	for bullet_bot in bullets_sq:
		bullet_bot.draw()

#MAIN_LOOP
sq = Player(50, 50, 20, 20, 8)
bot = Player_vs(ScreenWidth-sq.x-100, 0, 20, 20, 8)
bullets_sq = []
bullets_bot = []
shoot_loop = 0
sm = True

while sm:
	clock.tick(30)
	redrawWindow()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sm = False

#Limit of Boolets
	if shoot_loop > 0:
		shoot_loop += 1
	if shoot_loop > 3:
		shoot_loop = 0

#Boolets of player
	for bullet in bullets_sq:
		if bullet.y >= bot.y and bullet.y <= bot.y + bot.hitbox[3]:
			if bullet.x > bot.hitbox[0]:
				bot.hit()
				bullets_sq.pop()



		if bullet.x < ScreenWidth and bullet.x > 0 :
			bullet.x += bullet.vel
		else:
			if len(bullets_sq) != 0:
				bullets_sq.pop()
			else:
				continue

#Bullets of bot
	for bullet_bot in bullets_bot:
		if bullet_bot.y >= sq.y and bullet_bot.y <= sq.y + sq.hitbox[3]:
			if bullet_bot.x < sq.hitbox[0] + sq.hitbox[2]:
				sq.hit()
				bullets_bot.pop()



		if bullet_bot.x < ScreenWidth - 100 and bullet_bot.x > 0 :
			bullet_bot.x -= bullet_bot.vel
		else:
			bullets_bot.pop()

	keys = pygame.key.get_pressed()

#Shooting
	if len(bullets_bot) < 10 and shoot_loop == 0:
		bullets_bot.append(Bullet(bot.x, bot.y))
		shoot_loop = 1

	if keys[pygame.K_TAB] and shoot_loop == 0:
		if len(bullets_sq) < 10:
			bullets_sq.append(Bullet(sq.x+145, sq.y+52))
		shoot_loop = 1
#EXIT
	if keys[pygame.K_ESCAPE]:
		pygame.quit()
#MovingLeft	
	if keys[pygame.K_LEFT] and sq.x > sq.vel:
		sq.x -= sq.vel
		
#MovingRight
	if keys[pygame.K_RIGHT] and sq.x < ScreenWidth // 4.9:
		sq.x += sq.vel
		
#Up and Down	
	if keys[pygame.K_UP] and sq.y > sq.vel:
		sq.y -= sq.vel
	if keys[pygame.K_DOWN] and sq.y < ScreenHeight - 140:
		sq.y += sq.vel

#Bot Moving
	if bot.y <= 10:
		p = 1
	if bot.y + bot.hitbox[3] + 10 >= ScreenHeight:
		p = -1 
	bot.y += bot.vel * p


	
			
	
pygame.quit()