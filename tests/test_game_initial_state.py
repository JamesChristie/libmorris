import unittest

from libmorris.game   import tuple_list
from libmorris.game   import Game

from libmorris.errors import InvalidMove
from libmorris.errors import MoveOutOfBounds

class TestInitialGame(unittest.TestCase):
  def setUp(self):
    self.game       = Game()
    self.game_space = self.game.game_space

  def test_owner_of(self):
    self.assertTrue(
      all(self.game_space[position] == None for position in tuple_list())
    )
