import unittest

from libmorris.board  import tuple_list
from libmorris.board  import Board
from libmorris.player import Player

from libmorris.errors import InvalidMove, MoveOutOfBounds

class TestInitialBoard(unittest.TestCase):
  def setUp(self):
    self.game_space = Board().game_space

  def test_owner_of(self):
    self.assertTrue(
      all(self.game_space[position] == None for position in tuple_list())
    )
