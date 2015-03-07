import unittest

from libmorris.history import History
from libmorris.player  import Player

class TestHistoryAppending(unittest.TestCase):
  def setUp(self):
    self.history  = History()
    self.player   = Player(name="Some Lady")
    self.position = (0, 2)

    self.history.append(self.player, self.position)

  def test_move_count(self):
    self.assertEqual(self.history.move_count(), 1)

  def test_last_move(self):
    self.assertEqual(
      self.history.last_move(),
      {
        'player':   self.player,
        'position': self.position
      }
    )
