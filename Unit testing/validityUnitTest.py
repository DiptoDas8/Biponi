import unittest
from inputValidity import isValid

class validityTestCase(unittest.TestCase):
	def testIsGivenValidInput(self):
	#max_price, min_price
		self.assertTrue(isValid(67,7))	#max>min	--valid
	def testIsGivenValidInput2(self):
		self.assertFalse(isValid(5,7))
	def testIsGivenValidInput3(self):
		self.assertFalse(isValid("a",7))

if __name__ == '__main__':
	unittest.main()
