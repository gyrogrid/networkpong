import rpyc
import json
import socket
import sys
import SocketServer
from rpyc.utils.server import ThreadedServer
import os, pygame, math, random

from random import randint
from pygame.locals import *

serverstarted = 'no'
gamedata = {
	"ball_x": 0,
	"ball_y": 0,
	"ball_dx": 10,
	"ball_dy": 5,
	"pad1_x": 0,
	"pad1_y": 300,
	"pad2_x": 790,
	"pad2_y": 300,
	"score1": 0,
	"score2": 0
}	

class PongGame(rpyc.Service):	
	def on_connect(self):
		print('Connected To Server')

	def on_disconnect(self):
		print('disconnected')

	def exposed_movepad(self, direction, number):
		
		gamedata['ball_x'] += gamedata['ball_dx']
		gamedata['ball_y'] += gamedata['ball_dy']

		if gamedata['ball_y'] > 590 or gamedata['ball_y'] < 0:
			gamedata['ball_dy'] *= -1

		if gamedata['ball_x'] == gamedata['pad1_x'] and gamedata['ball_y'] == gamedata['pad1_y']:
			gamedata['ball_dy'] = gamedata['ball_dy'] * -1
		if gamedata['ball_x'] == gamedata['pad2_x'] and gamedata['ball_y'] == gamedata['pad2_y']:
			gamedata['ball_dy'] = gamedata['ball_dy'] * -1
		if gamedata['ball_x'] < gamedata['pad1_x']:
			gamedata['score1'] += 1
		if gamedata['ball_x'] > gamedata['pad2_x']:
			gamedata['score2'] += 1

		gamedata['ball_dx'] = randint(1,10)
		gamedata['ball_dy'] = randint(1,10)


		if direction == 'initial':
			return(gamedata)

		if number == 1:
			if direction == 'up' and gamedata['pad1_y'] > 0:
				gamedata['pad1_y'] -= 50
			if direction == 'down' and gamedata['pad1_y'] < 400:
				gamedata['pad1_y'] += 50
			
		if number == 2:
			if direction == 'up' and gamedata['pad2_y'] > 0:
				gamedata['pad2_y'] -= 50
			if direction == 'down' and gamedata['pad2_y'] < 400:
				gamedata['pad2_y'] += 50

		return(gamedata)



if __name__ == '__main__':
	server = ThreadedServer(PongGame, hostname = 'localhost', port = 12345)
	server.start()




