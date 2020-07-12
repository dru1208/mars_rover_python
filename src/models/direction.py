class Direction():

	def __init__(self, value):
		self.value = value

	def turn_right(self):
		if self.value == "N":
			self.value = "E"
		elif self.value =="E":
			self.value = "S"
		elif self.value == "S":
			self.value = "W"
		elif self.value == "W":
			self.value = "N"


