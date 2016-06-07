import unittest
from inputValidity import isValid

class validityTestCase(unittest.TestCase):
	def testIsGivenValidInput(self):
	#max_price, min_price
		self.assertTrue(isValid(67,7))	#max>min	--valid
<<<<<<< HEAD
	def testIsGivenValidInput2(self):
		self.assertFalse(isValid(5,7))
	def testIsGivenValidInput3(self):
=======
		self.assertFalse(isValid(5,7))
>>>>>>> 95d0d2b309f190152f39abf27546bc5ffdfe3b22
		self.assertFalse(isValid("a",7))

if __name__ == '__main__':
	unittest.main()
