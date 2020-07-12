import unittest
from src.models.direction import Direction


# this is an example of inheritance
# direction test inherits from unittest TestCase
class DirectionTest(unittest.TestCase):

	# test methods need to start with test_
	def test_turn_right(self):
		direction = Direction("N")
		direction.turn_right()
		self.assertEqual(direction.value, "E")

if __name__ == "__main__":
	unittest.main()