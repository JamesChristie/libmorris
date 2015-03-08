import unittest

from libmorris.game import Game

class TestGamePlayerRelations(unittest.TestCase):
  def setUp(self):
    self.game = Game()

  def test_opponent_for_player_one(self):
    self.assertEqual(
      self.game.opponent(self.game.player_one),
      self.game.player_two
    )

  def test_opponent_for_player_two(self):
    self.assertEqual(
      self.game.opponent(self.game.player_two),
      self.game.player_one
    )

  def test_get_last_player(self):
    self.assertIsNone(self.game.last_player)

  def test_current_player(self):
    self.assertEqual(
      self.game.current_player,
      self.game.player_one
    )
