#Red Object Tracking for python3
import io
import picamera
import pygame
from pygame.locals import *

debug = 1	#0:normal /1:debug
WIDTH = 480	#picture Width
HEIGHT = 360	#picture Height
margin = 50*debug
step = 2	#pixel size
dimw = int(WIDTH/step)
dimh = int(HEIGHT/step)
pygame.init()
DISPLAYSURF = pygame.display.set_mode((WIDTH+margin, HEIGHT+margin))
pygame.display.set_caption('Red Object Tracking')
camera = picamera.PiCamera()
camera.resolution = (WIDTH,HEIGHT)
stream = io.BytesIO()
WHITE = (255,255,255)
BLACK = (0,0,0)
RED =(255,0,0)
endflag = 0

while endflag==0:
	for event in pygame.event.get():
		if event.type == QUIT: endflag=1

	DISPLAYSURF.fill(BLACK)
	stream.seek(0)
	camera.capture(stream,'rgb')	#take a picture
	sumx = [0]*dimw
	sumy = [0]*dimh
	for y in range(0,HEIGHT,step):
		for x in range(0,WIDTH,step):
			stream.seek((x+(y*WIDTH))*3)
			r = ord(stream.read(1))     #red
			g = ord(stream.read(1))     #green
			b = ord(stream.read(1))     #blue
			rv = int(r-((g+b)/2))
			if rv<0 :rv=0
			sumx[int(x/step)] += rv
			sumy[int(y/step)] += rv
			pygame.draw.rect(DISPLAYSURF ,(r,g,b) ,(x,y,step,step))

	tx = step*(sumx.index(max(sumx)))
	ty = step*(sumy.index(max(sumy)))
	if debug:
		x = WIDTH
		for y in range(0,HEIGHT,step):
			ave = sumy[int(y/step)]/dimw
			pygame.draw.line(DISPLAYSURF ,RED,(x,y),(x+ave,y),1)

		y = HEIGHT
		for x in range(0,WIDTH,step):
			ave = sumx[int(x/step)]/dimh
			pygame.draw.line(DISPLAYSURF ,RED,(x,y),(x,y+ave),1)

		pygame.draw.line(DISPLAYSURF ,WHITE,(tx,0),(tx,HEIGHT),1)
		pygame.draw.line(DISPLAYSURF ,WHITE,(0,ty),(WIDTH,ty),1)
	else:
		pygame.draw.circle(DISPLAYSURF ,BLACK,(tx-30,ty-30),8)  #smile
		pygame.draw.circle(DISPLAYSURF ,BLACK,(tx+30,ty-30),8)
		pygame.draw.arc(DISPLAYSURF ,BLACK,(tx-30,ty-30,60,60),3.14,6.28,4)

	pygame.display.update()
pygame.quit()
camera.close()
