import unittest

from libmorris.history import History
from libmorris.player  import Player

class TestHistoryRewriting(unittest.TestCase):
  def setUp(self):
    self.history        = History()
    self.player_one     = Player(name="Some Lady")
    self.player_two     = Player(name="Some Other Lady")
    self.position_one   = (0, 2)
    self.position_two   = (1, 2)
    self.position_three = (2, 2)

    self.history.append(self.player_one, self.position_one)
    self.history.append(self.player_two, self.position_two)
    self.history.append(self.player_one, self.position_three)
    self.history.decrement()
    self.history.decrement()
    self.history.append(self.player_two, self.position_three)

  def test_move_count(self):
    self.assertEqual(self.history.move_count(), 2)

  def test_last_move(self):
    self.assertEqual(
      self.history.last_move(),
      {
        'player':   self.player_two,
        'position': self.position_three
      }
    )

  def test_get_move(self):
    self.assertEqual(
      self.history.get_move(1),
      {
        'player':   self.player_one,
        'position': self.position_one
      }
    )
