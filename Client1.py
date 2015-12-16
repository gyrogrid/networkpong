import rpyc
import json
import socket
import SocketServer
import sys
from rpyc.utils.server import ThreadedServer
import pygame
from pygame.locals import *


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

class Ball(pygame.sprite.Sprite):
	def __init__(self):
		#initialise the sprite
		pygame.sprite.Sprite.__init__(self)
		
		#create the image using the surface function, color it blue
		self.image = pygame.Surface([10, 10])
		self.image.fill(BLUE)

		#assign a rectangle, which is what we will use to move the image
		self.rect = self.image.get_rect()

class Pad(pygame.sprite.Sprite):
	def __init__(self):
		
		#initialise the sprite that represents the pad.
		pygame.sprite.Sprite.__init__(self)
		
		#create the image using the surface function, color it
		self.image = pygame.Surface([10, 200])
		self.image.fill(BLUE)
		self.rect = self.image.get_rect()


def main():
	conn = rpyc.connect('104.236.206.128', 12345, config={"allow_all_attrs": True})
	gamedata = conn.root.movepad('initial', 1)

	pygame.init()
	size = [800, 600]
	screen = pygame.display.set_mode(size)
	pygame.display.set_caption("Pong Yourself")
	pygame.mouse.set_visible(0)
	background = pygame.Surface(screen.get_size())
	font = pygame.font.Font(None, 30)

	ball = Ball()
	pad1 = Pad()
	pad2 = Pad()

	balls = pygame.sprite.Group()
	balls.add(ball)

	allsprites = pygame.sprite.RenderPlain((balls, pad1, pad2))
	clock = pygame.time.Clock()

	while 1:
		background.fill(BLACK)

		text = font.render("Player 1: ", True, WHITE)
		background.blit(text, (150,0))
		text = font.render("Player 2: ", True, WHITE)
		background.blit(text, (500,0))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			elif event.type == KEYDOWN and event.key == K_ESCAPE:
				return
			elif event.type == KEYDOWN and event.key == K_UP:
				gamedata = conn.root.movepad('up', 1)
			elif event.type == KEYDOWN and event.key == K_DOWN:
				gamedata = conn.root.movepad('down', 1)
							
		ball.rect.x = gamedata['ball_x']
		ball.rect.y = gamedata['ball_y']
		pad1.rect.x = gamedata['pad1_x']
		pad1.rect.y = gamedata['pad1_y']
		pad2.rect.x = gamedata['pad2_x']
		pad2.rect.y = gamedata['pad2_y']

		#Specify the fps, update the ball, blit everything to the screen and flip it. Flip is required to update the screen.
		clock.tick(60)
		screen.blit(background, (0, 0))
		allsprites.draw(screen)
		pygame.display.flip()

if __name__ == '__main__':
	main()