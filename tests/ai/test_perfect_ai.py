import unittest

from libmorris.game   import Game
from libmorris.player import Player

from libmorris.ai.perfect import Perfect

class TestEmptyGame(unittest.TestCase):
  def setUp(self):
    self.game = Game()

    self.game.game_space = {
      (1, 3): None, (2, 3): None, (3, 3): None,
      (1, 2): None, (2, 2): None, (3, 2): None,
      (1, 1): None, (2, 1): None, (3, 1): None
    }

    self.expected_move = (1, 2)

  def test_get_next_move(self):
    self.assertEqual(
      Perfect.get_perfect_move(
        self.game.player_one,
        self.game
      ),
      self.expected_move
    )

class TestNearWin(unittest.TestCase):
  def setUp(self):
    self.game = Game()

    self.game.game_space = {
      (1, 3): self.game.player_two, (2, 3): None, (3, 3): self.game.player_one,
      (1, 2): self.game.player_one, (2, 2): None, (3, 2): None,
      (1, 1): self.game.player_one, (2, 1): self.game.player_two, (3, 1): self.game.player_two
    }

    self.expected_move = (2, 2)

  def test_get_next_move(self):
    self.assertEqual(
      Perfect.get_perfect_move(
        self.game.player_one,
        self.game
      ),
      self.expected_move
    )

class TestNearLoss(unittest.TestCase):
  def setUp(self):
    self.game = Game()

    self.game.game_space = {
      (1, 3): None, (2, 3): self.game.player_two, (3, 3): None,
      (1, 2): None, (2, 2): None, (3, 2): self.game.player_two,
      (1, 1): self.game.player_one, (2, 1): self.game.player_one, (3, 1): self.game.player_two
    }

    self.expected_move = (3, 3)

  def test_get_next_move(self):
    self.assertEqual(
      Perfect.get_perfect_move(
        self.game.player_one,
        self.game
      ),
      self.expected_move
    )
