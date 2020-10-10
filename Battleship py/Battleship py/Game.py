from Position import Position
from Boat import Boat
from BoatBoard import BoatBoard
from AttackBoard import AttackBoard
from HUD import HUD
from Player import Player

class Game:
	def __init__(self, size, playersNum):
		self.players = []
		self.duration = 0
		self.isOver = False
		for i in range(playersNum):
			self.players.append(Player(size))

	def initiate(self):
		for player in self.players:
			for index in range(3):
				#tam = int(input("Tamaño del barco  "))-1
				tam = index +1
				posX = int(input("Posicion X del barco  "))
				posY = int(input("Posicion Y del barco  "))
				start = Position(posX,posY)
				dir = input("Direccion del barco [U,R,D,L]  ")
				
				if(dir == "U"): #Up
					posY -= tam
				elif(dir == "D"): #Down
					posY += tam
				elif(dir == "R"): #Right
					posX += tam
				elif(dir == "L"):	#Left
					posX -= tam
				end = Position(posX,posY)
				
				player.hud.boatsBoard.pushNewBoat(Boat(start,end))
				player.hud.mostrarBB()
			player.hud.mostrarHUD()

	def play(self):
		self.initiate()
        