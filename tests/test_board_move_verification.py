import unittest

from libmorris.board  import Board
from libmorris.player import Player

from libmorris.errors import InvalidMove, MoveOutOfBounds

class TestBoardMoveVerification(unittest.TestCase):
  def setUp(self):
    self.board    = Board()
    self.player   = Player(name="Some Dude")
    self.position = (2, 1)

  def test_move_request(self):
    self.board.request_move(self.player, self.position)

    self.assertFalse(self.board.is_position_free(self.position))
    self.assertTrue(self.board.is_position_taken(self.position))

    self.assertEqual(
        self.board.owner_of(self.position),
        self.player
    )

  def test_invalid_move_request(self):
    self.board.request_move(self.player, self.position)

    with self.assertRaises(InvalidMove):
      self.board.request_move(self.player, self.position)

  def test_out_of_bounds_move_request(self):
    with self.assertRaises(MoveOutOfBounds):
      self.board.request_move(self.player, (70, -403))
