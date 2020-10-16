from Position import Position
from Boat import Boat

class BoatBoard:
	def __init__(self, size):
		self.map = []
		for i in range(size):
			aux = []
			for ii in range(size):
				aux.append("O")
			self.map.append(aux)
		self.boats = []
		self.boatsLeft = 0
		self.tam = size

	def pushNewBoat(self, boat):
		self.boats.append(boat)
		for posi in boat.positions:
			self.map[posi.x][posi.y] = 1
		self.boatsLeft += 1
		return

	def sink(self,position):
		for ship in self.boats:
			for pos in ship.positions:
					if(pos == position):
							self.map[pos.x][pos.y] = -1
							ship.health -= 1
							#ship.remove(pos) arreglar el remove de la lista de posicion del ship
							if(ship.isAlive()==False):
									self.boats.remove(ship)
									self.boatsLeft -= 1
							return "Ø"
					else:
						self.map[pos.x][pos.y] = 2
		return "Õ"

	def __str__(self):
		return self.map
	def showMap(self):
		print("  0    1    2    3    4    5    6    7    8    9")
		print("╔════╦════╦════╦════╦════╦════╦════╦════╦════╦════╗")
		for ii in  range(self.tam):
			for i in range(self.tam):
				print("║",str(self.map[i][ii]) + ", ", end='',)
			print("║",ii)
			if (ii<=(self.tam-2)):
				print("╠════╬════╬════╬════╬════╬════╬════╬════╬════╬════╣")
		print ("╚════╩════╩════╩════╩════╩════╩════╩════╩════╩════╝")
	
