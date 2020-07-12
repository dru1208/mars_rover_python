import unittest
from src.models.direction import Direction


# this is an example of inheritance
# direction test inherits from unittest TestCase
class DirectionTest(unittest.TestCase):

	# test methods need to start with test_
	def test_turn_right(self):
		directionN = Direction("N")
		directionN.turn_right()
		self.assertEqual(directionN.value, "E")

		directionE = Direction("E")
		directionE.turn_right()
		self.assertEqual(directionE.value, "S")

		directionS = Direction("S")
		directionS.turn_right()
		self.assertEqual(directionS.value, "W")

		directionW = Direction("W")
		directionW.turn_right()
		self.assertEqual(directionW.value, "N")





if __name__ == "__main__":
	unittest.main()