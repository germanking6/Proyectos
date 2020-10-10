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
		i=0
		for player in self.players:
			i+=1
			print("jugador: ", i)
			posX=0
			posY=0
			for index in range(3):
				#tam = int(input("Tamaño del barco  "))-1
				tam = index +1
				#posX = int(input("Posicion X del barco  "))
				posX+=2
				#posY = int(input("Posicion Y del barco  "))
				posY=posX
				start = Position(posX,posY)
				#dir = input("Direccion del barco [U,R,D,L]  ")
				dir="D"
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

	def iniciarMovimientos(self):
		movimientos=0
		for player in self.players:
			while(self.players[0].hud.boatsBoard.boats!=0 or self.players[1].hud.boatsBoard.boats!=0 or movimientos>=4):
				self.movimientoPlayer2()
				self.movimientoPlayer1()

	def movimientoPlayer1(self):
		self.players[0].hud.mostrarHUD()
		print (self.players[1])
		posX = int(input("posicion a la cual quieres atacar x: "))
		posY= int(input("posicion a la cual quieres atacar y: "))
		pos=Position(posX,posY)
		self.players[0].attack(self.players[1], pos)

	def movimientoPlayer2(self):
		self.players[1].hud.mostrarHUD()
		print (self.players[0])
		posX = int(input("posicion a la cual quieres atacar x: "))
		posY= int(input("posicion a la cual quieres atacar y: "))
		pos=Position(posX,posY)
		self.players[1].attack(self.players[0], pos)
		self.players[1].hud.mostrarHUD()

	def play(self):
		self.initiate()
		self.iniciarMovimientos()