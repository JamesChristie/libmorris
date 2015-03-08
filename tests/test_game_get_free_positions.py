import unittest

from libmorris.game import Game

class TestGameGetFreePositions(unittest.TestCase):
  def setUp(self):
    self.game = Game()

    self.game.game_space = {
      (1, 3): 'X', (2, 3): None, (3, 3): 'X',
      (1, 2): 'O', (2, 2): None, (3, 2): 'O',
      (1, 1): 'O', (2, 1): None, (3, 1): 'O'
    }

    self.expected_positions = [(2, 3), (2, 2), (2, 1)]

  def test_get_free_positions(self):
    self.assertCountEqual(
      self.game.get_free_positions(),
      self.expected_positions
    )
