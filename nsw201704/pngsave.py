#PNG save
import pygame
from pygame.locals import *

colortable = [	#color(R,G,B)
	(0,0,0),		#0 black
	(0,0,255),		#1 blue
	(255,0,0),		#2 red
	(255,0,255),	#3 magenta
	(0,255,0),		#4 green
	(0,255,255),	#5 cyan
	(255,255,0),	#6 yellow
	(255,255,255)]	#7 white

chrdata = [	#character data
	"0000077777700000",
	"0000777557770000",
	"0007771111777000",
	"0072677777762700",
	"0772671111762770",
	"0772671111762770",
	"0772671111762770",
	"0772677777762770",
	"0072676666762700",
	"0007777777777000",
	"0007500750075000",
	"0075000750007500",
	"0750000750000750",
	"0750000750000750",
	"7750007755000755",
	"2220002222000222"]

PIXELSIZE = 16
BLUE = (0,0,255)
pygame.init()
surface = pygame.display.set_mode((320, 240))
surface.fill(BLUE)
array = pygame.PixelArray(surface)
for y in range(PIXELSIZE):
	for x in range(PIXELSIZE):
		num = int( chrdata[y][x] )
		array[x][y] = colortable[num]

del array
pygame.display.update()         #update screen
chrimage = surface.subsurface((0,0,PIXELSIZE,PIXELSIZE))
pygame.image.save(chrimage,"ship.png")
myclock = pygame.time.Clock()
endflag = 0
while endflag==0:
	for event in pygame.event.get():
		if event.type == QUIT: endflag=1

	myclock.tick(60)	#adjust fps

pygame.quit()
