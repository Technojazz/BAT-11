import math, random, sys
import pygame
from pygame.locals import *

(width, height) = (1276, 750)
running = True

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((width, height))

bat11 = pygame.image.load("Bat 11.png").convert_alpha()
batx = 630
baty = 363

angle = 180

laser1 = pygame.image.load("laser1.png").convert_alpha()
bx = 0
bx2 = 0
by = 0
by2 = 0
bz = False
bz2 = False
shoot = True
shoot2 = True
shoottime = 660
shoottime2 = -330

androne = pygame.image.load("Androne.png").convert_alpha()

roid = [pygame.image.load("asteroidS.png").convert_alpha(),
 pygame.image.load("asteroidM.png").convert_alpha(),
  pygame.image.load("asteroidL.png").convert_alpha()]

FPS = 120

space = pygame.image.load("space.png").convert_alpha()
x = -319
y = -187.5
	
class Drone:

	def __init__(self, dronex, droney):
		self.x = dronex
		self.y = droney

dlist = []	
for i in range(10):
	dronex = random.randint(0, 7700)
	droney = random.randint(0, 4520)
	dlist.append(Drone (dronex, droney))

class Roid:
	
	def __init__(self, roidx, roidy):
		self.x = roidx
		self.y = roidy
		self.type = random.randint(0, 2)

rlist = []
for i in range(811):
	roidx = random.randint(-1000, 9104)
	roidy = random.randint(-800, 7200)
	rlist.append(Roid(roidx, roidy))

class Laser1:
	
	def __init__(self, beamx, beamy):
		self.x = beamx
		self.y = beamy

blist = []
for i in range(1):
	beamx = batx
	beamy = baty
	blist.append(Laser1(beamx, beamy))

class Laser2:

	def __init__(self, beamx2, beamy2):
		self.x2 = beamx2
		self.y2 = beamy2

b2list = []
for i in range(1):
	beamx2 = batx
	beamy2 = baty
	b2list.append(Laser2(beamx2, beamy2))

while True:
	for b in blist:
		if bz == False:
			screen.blit(laser1, (b.x, b.y))
		else:
			continue
	
	for b2 in b2list:
		if bz2 == False:
			screen.blit(laser1, (b2.x2, b2.y2))
		else:
			continue
	
	screen.blit(space, (x, y))
	
	for b in blist:
		if bz == True:
			screen.blit(laser1, (b.x, b.y))
		else:
			continue

	for b2 in b2list:
		if bz2 == True:
			screen.blit(laser1, (b2.x2, b2.y2))
		else:
			continue

	screen.blit(bat11, (batx, baty))
	
	for r in rlist:
		screen.blit(roid[r.type], (r.x, r.y))
	
	for d in dlist:
		screen.blit(androne, (d.x, d.y))

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
					laser1 = pygame.transform.rotate(laser1, 180)
					pygame.display.update()
				elif angle == 180:
					angle = 90
					bat11 = pygame.transform.rotate(bat11, 90)
					laser1 = pygame.transform.rotate(laser1, 90)
					pygame.display.update()
				elif angle == -180:
					angle = 90
					bat11 = pygame.transform.rotate(bat11, -90)
					laser1 = pygame.transform.rotate(laser1, -90)
					pygame.display.update()

			if event.key == pygame.K_RIGHT:
				if angle == -90:
					continue
				elif angle == 90:
					angle = -90
					bat11 = pygame.transform.rotate(bat11, 180)
					laser1 = pygame.transform.rotate(laser1, 180)
					pygame.display.update()
				elif angle == 180:
					angle = -90
					bat11 = pygame.transform.rotate(bat11, -90)
					laser1 = pygame.transform.rotate(laser1, -90)
					pygame.display.update()
				elif angle == -180:
					angle = -90
					bat11 = pygame.transform.rotate(bat11, 90)
					laser1 = pygame.transform.rotate(laser1, 90)
					pygame.display.update()

			if event.key == pygame.K_UP:
				if angle == 180:
					continue
				elif angle == 90:
					angle = 180
					bat11 = pygame.transform.rotate(bat11, -90)
					laser1 = pygame.transform.rotate(laser1, -90)
					pygame.display.update()
				elif angle == -90:
					angle = 180
					bat11 = pygame.transform.rotate(bat11, 90)
					laser1 = pygame.transform.rotate(laser1, 90)
					pygame.display.update()
				elif angle == -180:
					angle = 180
					bat11 = pygame.transform.rotate(bat11, 180)
					laser1 = pygame.transform.rotate(laser1, 180)
					pygame.display.update()

			if event.key == pygame.K_DOWN:
				if angle == -180:
					continue
				elif angle == 90:
					angle = -180
					bat11 = pygame.transform.rotate(bat11, 90)
					laser1 = pygame.transform.rotate(laser1, 90)
					pygame.display.update()
				elif angle == -90:
					angle = -180
					bat11 = pygame.transform.rotate(bat11, -90)
					laser1 = pygame.transform.rotate(laser1, -90)
					pygame.display.update()
				elif angle == 180:
					angle = -180
					bat11 = pygame.transform.rotate(bat11, 180)
					laser1 = pygame.transform.rotate(laser1, 180)
					pygame.display.update()
	
			if event.key == pygame.K_a:
				if shoot == True:
					shoot = False
					bz = True
					b.x = batx
					b.y = baty
					pygame.display.update()
					if angle == 180:
						bx = 0
						by = -15
					elif angle == 90:
						bx = -15
						by = 0
					elif angle == -90:
						bx = 15
						by = 0
					elif angle == -180:
						bx = 0
						by = 15
				elif shoot2 == True:
					shoot2 = False
					bz2 = True
					if angle == 180:
						b2.x2 = batx + 15
						b2.y2 = baty
						pygame.display.update()
						bx2 = 0
						by2 = -15
					elif angle == 90:
						b2.x2 = batx
						b2.y2 = baty + 15
						pygame.display.update()
						bx2 = -15
						by2 = 0
					elif angle == -90:
						b2.x2 = batx
						b2.y2 = baty + 15
						pygame.display.update()
						bx2 = 15
						by2 = 0
					elif angle == -180:
						b2.x2 = batx + 15
						b2.y2 = baty
						pygame.display.update()
						bx2 = 0
						by2 = 15
				else:
					continue

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
		b.x += bx
		b.y += by

	for b2 in b2list:
		b2.x2 += xdiff * 2
		b2.y2 += ydiff * 2
		b2.x2 += bx2
		b2.y2 += by2

	for d in dlist:
		d.x += xdiff * 2
		d.y += ydiff * 2

		if batx > d.x:
			d.x += 1
			if batx > d.x:
				d.x += 1
		elif batx < d.x:
			d.x -= 1
			if batx < d.x:
				d.x -= 1
			
		if baty > d.y:
			d.y += 1
			if baty > d.y:
				d.y += 1
		elif baty < d.y:
			d.y -= 1
			if baty < d.y:
				d.y -= 1

	for r in rlist:
		r.x += xdiff * 2
		r.y += ydiff * 2

	if shoottime >= 1320:
		shoot = True
		shoottime = 660
		bz = False
	else:
		shoottime += 15

	if shoottime2 >= 1320:
		shoot2 = True
		shoottime2 = 660
		bz2 = False
	else:
		shoottime2 += 15

	pygame.display.update()
	clock.tick(FPS)
