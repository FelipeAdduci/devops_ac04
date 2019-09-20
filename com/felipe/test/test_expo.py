from unittest import TestCase
from com.felipe.expo import pot

class TestPot(TestCase):
	def setUp(self):
		self.expo = pot()
		
	def test_pot(self):
		self.assertEqual(self.expo.pot(1,5),1, "O resultado deveria ser 1")