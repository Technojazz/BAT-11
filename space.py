import math, random, sys
import pygame
from pygame.locals import *

collision_rate = 0

(width, height) = (1276, 750)
running = True

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((width, height))

pygame.mouse.set_visible(False)

bat11 = pygame.image.load("Bat 11.png").convert_alpha()
batx = 630
baty = 363

angle = 180

roid = [pygame.image.load("asteroidS.png").convert_alpha(),
 pygame.image.load("asteroidM.png").convert_alpha(),
  pygame.image.load("asteroidL.png").convert_alpha()]

FPS = 120

space = pygame.image.load("space.png").convert_alpha()
x = -319
y = -187.5

lvl_one = 5
lvl = lvl_one

class Drone:

	def __init__(self):
		self.x = random.randint(0, 7700)
		self.y = random.randint(0, 4520)
		self.hp = 3
		self.androne = pygame.image.load("Androne.png").convert_alpha()

dlist = []
for i in range(5):
	dlist.append(Drone())

class Roid:
	
	def __init__(self, roidx, roidy):
		self.x = roidx
		self.y = roidy
		self.type = random.randint(0, 2)

rlist = []
for i in range(811):
	roidx = random.randint(-1000, 9104)
	roidy = random.randint(-800, 7200)
	rlist.append(Roid (roidx, roidy))

class Laser:
	
	def __init__(self):
		self.x = batx
		self.y = baty
		self.z = False
		self.angle = angle
		self.laser1 = pygame.image.load("laser1.png").convert_alpha()

	def collide(self, rect):
		self.rect = self.laser1.get_rect(left=(self.x), top=(self.y))
		self.c = self.rect.colliderect(d.rect)
		return self.c

blist = []
for i in range(1):
	blist.append(Laser())

while running:
	for b in blist:
		if b.z == False:
			continue

	screen.blit(space, (x, y))
	
	for b in blist:
		if b.z == True:
			screen.blit(b.laser1, (b.x, b.y))
		else:
			continue

	screen.blit(bat11, (batx, baty))
	
	for r in rlist:
		screen.blit(roid[r.type], (r.x, r.y))
	
	for d in dlist:
		screen.blit(d.androne, (d.x, d.y))
		print(d.x, d.y)
	print()
	print(batx, baty)
	print()
	print()

	for event in pygame.event.get():
		if event.type==QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
			sys.exit()
		if event.type == pygame.KEYDOWN:
			
			if event.key == pygame.K_LEFT:
				if angle == 90:
					continue
				elif angle == -90:
					angle = 90
					bat11 = pygame.transform.rotate(bat11, 180)
					pygame.display.update()
				elif angle == 180:
					angle = 90
					bat11 = pygame.transform.rotate(bat11, 90)
					pygame.display.update()
				elif angle == -180:
					angle = 90
					bat11 = pygame.transform.rotate(bat11, -90)
					pygame.display.update()

			if event.key == pygame.K_RIGHT:
				if angle == -90:
					continue
				elif angle == 90:
					angle = -90
					bat11 = pygame.transform.rotate(bat11, 180)
					pygame.display.update()
				elif angle == 180:
					angle = -90
					bat11 = pygame.transform.rotate(bat11, -90)
					pygame.display.update()
				elif angle == -180:
					angle = -90
					bat11 = pygame.transform.rotate(bat11, 90)
					pygame.display.update()

			if event.key == pygame.K_UP:
				if angle == 180:
					continue
				elif angle == 90:
					angle = 180
					bat11 = pygame.transform.rotate(bat11, -90)
					pygame.display.update()
				elif angle == -90:
					angle = 180
					bat11 = pygame.transform.rotate(bat11, 90)
					pygame.display.update()
				elif angle == -180:
					angle = 180
					bat11 = pygame.transform.rotate(bat11, 180)
					pygame.display.update()

			if event.key == pygame.K_DOWN:
				if angle == -180:
					continue
				elif angle == 90:
					angle = -180
					bat11 = pygame.transform.rotate(bat11, 90)
					pygame.display.update()
				elif angle == -90:
					angle = -180
					bat11 = pygame.transform.rotate(bat11, -90)
					pygame.display.update()
				elif angle == 180:
					angle = -180
					bat11 = pygame.transform.rotate(bat11, 180)
					pygame.display.update()
	
			#if event.key == pygame.K_a:


	keys_pressed = pygame.key.get_pressed()
	xdiff = 0
	ydiff = 0
	if keys_pressed[K_LEFT]:
		if x >= 0:
			continue
		elif keys_pressed[K_LSHIFT]:
			xdiff += 5
		else:
			xdiff += 2
	if keys_pressed[K_RIGHT]:
		if x <= -3825:
			continue
		elif keys_pressed[K_LSHIFT]:
			xdiff -= 5
		else:
			xdiff -= 2
	if keys_pressed[K_UP]:
		if y >= 0:
			continue
		elif keys_pressed[K_LSHIFT]:
			ydiff += 5
		else:
			ydiff += 2
	if keys_pressed[K_DOWN]:
		if y <= -2250:
			continue
		elif keys_pressed[K_LSHIFT]:
			ydiff -= 5
		else:
			ydiff -= 2

	x += xdiff
	y += ydiff

	for b in blist:
		b.x += xdiff * 2
		b.y += ydiff * 2

	for d in dlist:
		d.x += xdiff * 2
		d.y += ydiff * 2

 

		if batx > d.x:
			d.x += 1
			if batx > d.x:
				d.x += 1
		
		if batx < d.x:
			d.x -= 1
			if batx < d.x:
				d.x -= 1
				
		if (batx > d.x) > (baty > d.y):
			d.x += 2
		
		if (batx < d.x) > (baty < d.y):
			d.x -= 2

		if (batx > d.x) > (baty < d.y):
			d.x += 2
		
		if (batx < d.x) > (baty > d.y):
			d.x -= 2

		if baty > d.y:
			d.y += 1
			if baty > d.y:
				d.y += 1
		
		if baty < d.y:
			d.y -= 1
			if baty < d.y:
				d.y -= 1
				
		if (baty > d.y) > (batx > d.x):
			d.y += 2
		
		if (baty < d.y) > (batx < d.x):
			d.y -= 2

		if (baty > d.y) > (batx < d.x):
			d.y += 2
		
		if (baty < d.y) > (batx > d.x):
			d.y -= 2

	for r in rlist:
		r.x += xdiff * 2
		r.y += ydiff * 2

	for d in dlist:
		d.rect = d.androne.get_rect(left=(d.x), top=(d.y))
		for b in blist:
			if b.collide(d.rect) == True:
				print("Collision!")
				collision_rate += 1

	pygame.display.update()
	clock.tick(FPS)