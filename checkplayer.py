import unittest

from player import Player

class CheckPlayer(unittest.TestCase):

	def test_player_name(self):
		player = Player('Player')
		self.assertEqual(player.get_name(),'Player')
		self.assertFalse(player.get_is_computer())

	def test_player_name_computer(self):
		player = Player('Player', True)
		self.assertEqual(player.get_name(),'Player')
		self.assertTrue(player.get_is_computer())

	def test_player_number_of_attempts(self):
		player = Player('Player')
		player.set_number_of_attempts(2)
		self.assertEqual(player.get_number_of_attempts(),2)

	def test_player_set_playing(self):
		player = Player('Player')
		player.set_playing(True)
		self.assertTrue(player.get_playing())

	def test_player_add_feedback(self):
		player = Player('Player')
		player.add_feedback('Code','Feedback')
		feedback_list = player.get_feedback_list()
		self.assertTrue(len(feedback_list)==1)
		self.assertTrue(feedback_list[0].get_code_entered() == 'Code')
		self.assertTrue(feedback_list[0].get_feedback_given() == 'Feedback')

	def test_player_set_successful(self):
		player = Player('Player')
		player.set_successful(True)
		self.assertTrue(player.get_successful())


	def evaluate_code(self, code):
		player = Player('Player')
		player.set_code('Code')
		self.assertTrue(player.evaluate_code('Code') == None)

	def evaluate_code_incorrect(self, code):
		player = Player('Player')
		player.set_code('Code')
		self.assertTrue(player.evaluate_code('Codd') == 'KKK')

unittest.main()
