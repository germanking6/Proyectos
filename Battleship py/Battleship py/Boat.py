from Position import Position

class Boat:
	def __init__(self, head, tail):

		print("Head: (" + str(head.x) + ", " + str(head.y) + ")")
		print("Tail: (" + str(tail.x) + ", " + str(tail.y) + ")")
		print("-----------")
		self.head = head
		self.tail = tail
		self.positions = list()
		if(head.x != tail.x):
				for i in range(min(head.x,tail.x),max(tail.x,head.x)+1):
						aux = Position(i, head.y)
						self.positions.append(aux)
		else:
				for i in range(min(head.y,tail.y),max(tail.y,head.y)+1):
						aux = Position(head.x, i)
						self.positions.append(aux)

		self.size = len(self.positions)
		self.health = self.size
	def isAlive(self):
			if(self.health == 0):
					return False
			return True