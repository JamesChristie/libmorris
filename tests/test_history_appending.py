import unittest

from libmorris.history import History
from libmorris.player  import Player

class TestHistoryAppending(unittest.TestCase):
  def setUp(self):
    self.history        = History()
    self.player_one     = Player(name="Some Lady")
    self.player_two     = Player(name="Some Other Lady")
    self.position_one   = (0, 2)
    self.position_two   = (1, 2)
    self.position_three = (2, 2)

  def test_append_move(self):
    self.history.append(self.player_one, self.position_one)

    self.assertEqual(self.history.move_count(), 1)

    self.assertEqual(
      self.history.last_move(),
      {
        'player':   self.player_one,
        'position': self.position_one
      }
    )

  def test_decrement_move(self):
    self.history.append(self.player_one, self.position_one)
    self.history.append(self.player_two, self.position_two)
    self.history.decrement()

    self.assertEqual(self.history.move_count(), 2)

    self.assertEqual(self.history.current_move, 2)

    self.assertEqual(
      self.history.last_move(),
      {
        'player':   self.player_one,
        'position': self.position_one
      }
    )

    self.assertEqual(
      self.history.get_move(2),
      {
        'player':   self.player_two,
        'position': self.position_two
      }
    )

  def test_rewriting_move_history(self):
    self.history.append(self.player_one, self.position_one)
    self.history.append(self.player_two, self.position_two)
    self.history.append(self.player_one, self.position_three)
    self.history.decrement()
    self.history.decrement()
    self.history.append(self.player_two, self.position_three)

    self.assertEqual(self.history.move_count(), 2)

    self.assertEqual(
      self.history.last_move(),
      {
        'player':   self.player_two,
        'position': self.position_three
      }
    )

    self.assertEqual(
      self.history.get_move(1),
      {
        'player':   self.player_one,
        'position': self.position_one
      }
    )
