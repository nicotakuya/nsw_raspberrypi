#USB gamepad test
import pygame
BLACK	= ( 0,   0,   0)
WHITE	= ( 255, 255, 255)
WIDTH = 320
HEIGHT = 240
pygame.init()
surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.joystick.init()
print("get_count : "+str( pygame.joystick.get_count() ))
joystick_id = 0
joystick = pygame.joystick.Joystick(joystick_id)
joystick.init()
print("get_name : "+joystick.get_name())
print("get_numaxes : "+str( joystick.get_numaxes() ))
print("get_numbuttons : "+str( joystick.get_numbuttons() ))
print("get_numhats : " +str( joystick.get_numhats() ))
myfont = pygame.font.Font(None, 30)
myclock = pygame.time.Clock()
endflag = 0
while endflag==0:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: endflag=1
 
	ax = joystick.get_axis( 0 )
	surface.fill(WHITE)
	bitmaptext = myfont.render("axis : "+str(ax), True, BLACK)
	surface.blit(bitmaptext, (50, 100))
	pygame.display.update()         #Update Screen
	myclock.tick(60)	#Adjust frames per second
pygame.quit ()
