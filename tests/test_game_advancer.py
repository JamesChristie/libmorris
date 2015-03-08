import unittest

from libmorris.game          import Game
from libmorris.game_advancer import GameAdvancer

class TestGameAdvancerForLambdaPlayer(unittest.TestCase):
  def setUp(self):
    self.position = (1, 1)
    self.game     = Game(hook_one=lambda game: (1, 1))

    GameAdvancer.resolve_next_turn(self.game)

  def test_updated_game(self):
    self.assertEqual(
      self.game.owner_of(self.position),
      self.game.player_one
    )

class TestGameAdvancerForAIPlayer(unittest.TestCase):
  def setUp(self):
    self.position = (1, 2)
    self.game     = Game()

    GameAdvancer.resolve_next_turn(self.game)

  def test_updated_game(self):
    self.assertEqual(
      self.game.owner_of(self.position),
      self.game.player_one
    )
