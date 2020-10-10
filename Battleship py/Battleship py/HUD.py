from BoatBoard import BoatBoard
from AttackBoard import AttackBoard

class HUD:
	def __init__(self, size):
		self.boatsBoard = BoatBoard(size)
		self.attackBoard = AttackBoard(size)

	def mostrarHUD(self):
		print("HUD\nBoat Board")
		self.boatsBoard.showMap()
		print("Atack Board")
		self.attackBoard.showMap()
	
	def mostrarBB(self):
		print("Boat Board")
		self.boatsBoard.showMap()

	def mostrarAB(self):
		print("Atack Board")
		self.attackBoard.showMap()