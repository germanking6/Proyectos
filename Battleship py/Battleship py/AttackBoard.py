from Position import Position

class AttackBoard:
	def __init__(self, size):
		self.map = []
		for i in range(size):
			aux = []
			for ii in range(size):
					aux.append(0)
			self.map.append(aux)
			self.tam = size

	def bombard(self, pos, val):
		self.map[pos.x][pos.y] += val
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