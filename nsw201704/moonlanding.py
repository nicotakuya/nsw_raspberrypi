#Moon landing
import pygame
from pygame.locals import *
import math
import random

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WIDTH = 640	#screen width
HEIGHT = 480	#screen height
ground = [(0,479),(150,300),(300,430),(420,430),(500,350),(639,479)]
goal = (330,430,60,10)
star = []
for i in range(30):
	star.append((random.randint(0,WIDTH-1),random.randint(0,HEIGHT-1),2,2))

pygame.init()
surface = pygame.display.set_mode((WIDTH ,HEIGHT))
pygame.joystick.init()
joystick_count = pygame.joystick.get_count()
if joystick_count == 0: print("Error: joystick not found")
joystick_id = 0
joystick = pygame.joystick.Joystick(joystick_id)
joystick.init()
chrimage = pygame.image.load("ship.png")
chrimage.set_colorkey(BLACK ,RLEACCEL)
x = 160
y = 16
x1 = 0
y1 = 0
scale = 2
angle = 0
message = ""
myfont = pygame.font.Font(None, 70)
myclock = pygame.time.Clock()
endflag = 0
while endflag==0:
	for event in pygame.event.get():
		if event.type == QUIT: endflag = 1

	surface.fill(BLACK)
	for i in range(30):
		pygame.draw.rect(surface, BLUE ,star[i])

	pygame.draw.polygon(surface ,GREEN , ground)
	pygame.draw.rect(surface, RED, goal)
	if message=="":
		col = surface.get_at((int(x), int(y+16)))
		if col.g >= 255: message="failed!"
		if col.r >= 255:
			if y1 >= 0.5:
				message="failed!"
			else:
				message="succeeded!"

		ax = joystick.get_axis( 0 )	#Get axis X
		ay = joystick.get_axis( 1 )	#Get axis Y
		if math.fabs(ax) >= 0.2: angle = angle-ax
		boost = -ay
		if boost < 0.2: boost = 0
		rd = math.radians(-angle-90)
		x1 = x1+(math.cos(rd)*boost/100)
		y1 = y1+(math.sin(rd)*boost/100)
		xb = int(x-math.cos(rd)*16)
		yb = int(y-math.sin(rd)*16)
		r = int(16*boost)
		pygame.draw.circle(surface ,WHITE ,(xb,yb) ,r)
		y1 = y1+0.005	#gravity
		x = x+x1
		y = y+y1
		if x < 0 :x = 0
		if x > WIDTH-1 :x = WIDTH-1
		if y < 0 :y = 0
		if y > HEIGHT-1 :y = HEIGHT-1

	chrimage2 = pygame.transform.rotozoom(chrimage ,angle ,scale)
	chrw = chrimage2.get_width()
	chrh = chrimage2.get_height()	
	surface.blit(chrimage2 ,(x-(chrw/2) ,y-(chrh/2)))
	bitmaptext = myfont.render(message ,True ,WHITE)
	surface.blit(bitmaptext ,(200,240))
	pygame.display.update()
	myclock.tick(60)
pygame.quit()
