import unittest

from libmorris.game import Game

class TestGameCopy(unittest.TestCase):
  def setUp(self):
    self.game = Game()
    self.copy = self.game.get_copy()

  def test_mutate_copy(self):
    self.copy.game_space[(1, 1)] = "Testing"
    
    self.assertEqual(
      self.copy.game_space[(1, 1)],
      "Testing"
    )

    self.assertIsNone(self.game.game_space[(1, 1)])

  def test_player_one(self):
    self.assertEqual(
      self.game.player_one,
      self.game.player_one
    )

  def test_player_two(self):
    self.assertEqual(
      self.game.player_two,
      self.game.player_two
    )
